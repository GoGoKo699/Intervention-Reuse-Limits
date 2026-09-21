#!/usr/bin/env python3
"""Deterministic checks of the intervention-reuse construction.

No trajectories are sampled, no training is performed, and no network is used.
Conventions: row generators Q; column probabilities obey p'=Q.T @ p;
response coefficients multiply h**j (they are derivatives divided by j!).
Run: python verify.py --output verification_report.json
"""
from __future__ import annotations
import argparse
import json
import math
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm
from scipy.integrate import solve_ivp
import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def symbolic_checks() -> dict:
    h, z = sp.symbols('h z', real=True)
    r, k = sp.symbols('r k', positive=True)
    Q = sp.Matrix([[0, k*sp.exp(2*h)/2, k/2],
                   [k, 0, r], [k*sp.exp(-2*h), r, 0]])
    for i in range(3):
        Q[i,i] = -sum(Q[i,j] for j in range(3) if j != i)
    pi = sp.Matrix([1, sp.exp(2*h)/2, sp.exp(2*h)/2])/(1+sp.exp(2*h))
    require(Q*sp.ones(3,1) == sp.zeros(3,1), 'Symbolic row sums')
    db = sp.diag(*pi)*Q-Q.T*sp.diag(*pi)
    require(all(sp.simplify(x)==0 for x in db), 'Symbolic detailed balance')
    require(all(sp.simplify(x)==0 for x in Q.T*pi), 'Symbolic stationarity')
    Q0 = Q.subs(h,0)
    C = sp.Matrix([[1,0],[0,1],[0,1]])
    Kvis = sp.Matrix([[-k,k],[k,-k]])
    require(Q0*C == C*Kvis, 'Exact passive lumpability')
    require(sp.simplify(Q[1,0]-Q[2,0]) == k-k*sp.exp(-2*h),
            'Nonzero-field exit-rate contrast')
    p0=sp.Matrix([sp.Rational(1,2),sp.Rational(1,4),sp.Rational(1,4)])
    f=sp.Matrix([-1,1,1])
    exact=[]
    for rr in (sp.Rational(1,4),sp.Rational(1,2),sp.Integer(1)):
        B=[Q.diff(h,j).subs({h:0,k:1,r:rr})/sp.factorial(j) for j in range(4)]
        R=(z*sp.eye(3)-B[0].T).inv()
        pp=[R*p0]
        for j in range(1,4):
            pp.append(R*sum((B[l].T*pp[j-l] for l in range(1,j+1)),sp.zeros(3,1)))
        out=[sp.factor((f.T*x)[0]) for x in pp]
        target=[0,2/(z*(z+2)),0,
                -sp.Rational(1,3)/z+sp.Rational(1,3)/(z+2)+2/(z+2)**2
                -2/((z+2)**2*(z+1+2*rr))]
        require(all(sp.factor(a-b)==0 for a,b in zip(out,target)),
                f'Exact Laplace coefficients r={rr}')
        exact.append({'r':str(rr),'laplace_m3':str(out[3]),'status':'PASS'})
    t=sp.symbols('t', real=True)
    m3=-sp.Rational(1,3)+(sp.Rational(25,3)+6*t)*sp.exp(-2*t)-8*sp.exp(-3*t/2)
    baseline=-sp.Rational(1,3)+(sp.Rational(1,3)+t)*sp.exp(-2*t)
    recovered=sp.simplify(-sp.exp(-t)*sp.diff(sp.exp(2*t)*(m3-baseline),t,2)/2)
    require(sp.simplify(recovered-sp.exp(-t/2))==0,'Exact kernel inversion')
    return {'generator_and_balance':'PASS','passive_lumpability':'PASS',
            'laplace_cases':exact,'three_state_kernel_inversion':'PASS'}


def generator_coefficients(k: float, mu: np.ndarray, H: np.ndarray,
                           g: np.ndarray, order: int=3) -> list[np.ndarray]:
    """Taylor coefficients Q_l for rates A->Bj=k mu_j exp[(1+g_j)h]."""
    m=len(mu)
    require(H.shape==(m,m) and g.shape==(m,), 'Array dimensions')
    require(np.all(mu>0) and abs(mu.sum()-1)<1e-12, 'Positive normalized mu')
    require(abs(mu@g)<1e-12,'Centered kinetic sensitivity')
    require(np.max(abs(H.sum(axis=1)))<1e-12,'Hidden generator row sums')
    out=[]
    for ell in range(order+1):
        Q=np.zeros((m+1,m+1))
        Q[0,1:]=k*mu*(1+g)**ell/math.factorial(ell)
        Q[1:,0]=k*(g-1)**ell/math.factorial(ell)
        if ell==0:
            Q[1:,1:]=H
            np.fill_diagonal(Q,0.0)
        np.fill_diagonal(Q,-Q.sum(axis=1))
        out.append(Q)
    return out


def full_generator(h:float,k:float,mu:np.ndarray,H:np.ndarray,g:np.ndarray)->np.ndarray:
    Q=np.zeros((len(mu)+1,len(mu)+1))
    Q[0,1:]=k*mu*np.exp((1+g)*h)
    Q[1:,0]=k*np.exp((g-1)*h)
    Q[1:,1:]=H
    np.fill_diagonal(Q,0.0)
    np.fill_diagonal(Q,-Q.sum(axis=1))
    return Q


def hidden_spectrum(mu:np.ndarray,H:np.ndarray,g:np.ndarray)->tuple[np.ndarray,np.ndarray]:
    root=np.sqrt(mu)
    S=root[:,None]*H/root[None,:]
    require(np.max(abs(S-S.T))<1e-12,'Hidden detailed balance')
    lam,V=np.linalg.eigh(-S)
    w=(V.T@(root*g))**2
    keep=lam>1e-10
    return lam[keep], w[keep]


def phi(d:np.ndarray,t:float)->np.ndarray:
    ans=np.empty_like(d)
    close=abs(d*t)<1e-4
    # Stable Taylor series of (exp(dt)-1-dt)/d^2, including d=0.
    ans[close]=t*t*sum((d[close]*t)**j/math.factorial(j+2) for j in range(9))
    ans[~close]=(np.expm1(d[~close]*t)-d[~close]*t)/(d[~close]**2)
    return ans


def predicted_coefficients(t:float,k:float,lam:np.ndarray,w:np.ndarray)->np.ndarray:
    decay=np.exp(-2*k*t)
    m1=-np.expm1(-2*k*t)
    base=-m1/3+k*t*decay
    correction=decay*(k*w.sum()*t-2*k*k*np.dot(w,phi(k-lam,t)))
    return np.array([0.,m1,0.,base+correction])


def block_matrix(B:list[np.ndarray],u:float=1.)->np.ndarray:
    n=B[0].shape[0]; degree=len(B)
    A=np.zeros((degree*n,degree*n))
    for j in range(degree):
        for ell in range(j+1):
            A[j*n:(j+1)*n,(j-ell)*n:(j-ell+1)*n]=B[ell].T*u**ell
    return A


def path_model(m:int)->tuple[float,np.ndarray,np.ndarray,np.ndarray]:
    k=1.; rate=.1; mu=np.ones(m)/m
    H=np.zeros((m,m))
    for i in range(m-1): H[i,i+1]=H[i+1,i]=rate
    np.fill_diagonal(H,-H.sum(axis=1))
    g=np.zeros(m);g[0]=1.;g-=mu@g
    return k,mu,H,g


def deterministic_checks()->dict:
    max_error=0.;n_cases=0;dimensions=[]
    models=[path_model(m) for m in range(2,9)]
    # Additional nonsymmetric row generator, reversible with nonuniform mu.
    mu=np.array([.1,.2,.3,.4]);H=np.zeros((4,4))
    for i,c in enumerate([.004,.007,.009]):
        H[i,i+1]=c/mu[i];H[i+1,i]=c/mu[i+1]
    np.fill_diagonal(H,-H.sum(axis=1))
    g=np.array([.8,-.2,.4,-.7]);g-=mu@g
    models.append((1.,mu,H,g))
    for k,mu,H,g in models:
        B=generator_coefficients(k,mu,H,g);n=len(mu)+1
        p0=np.r_[.5,.5*mu];f=np.r_[-1.,np.ones(len(mu))]
        lam,w=hidden_spectrum(mu,H,g)
        require(np.max(abs(B[0].T@p0))<1e-12,'Stationary p0')
        if np.allclose(mu,np.ones(len(mu))/len(mu)):
            expected=2*.1*(1-np.cos(np.pi*np.arange(1,len(mu))/len(mu)))
            require(np.max(abs(lam-expected))<1e-12,'Path eigenvalues')
            require(np.all(w>1e-12),'Every hidden mode has positive weight')
            require(np.all(lam<k),'No visible/hidden pole collision')
            dimensions.append({'microscopic_states':n,'passive_states':2,
                               'distinct_response_poles':len(lam)+2,
                               'min_hidden_weight':float(w.min())})
        y0=np.zeros(4*n);y0[:n]=p0;A=block_matrix(B)
        for t in [0.,.05,.2,.7,1.,2.5,5.]:
            y=expm(t*A)@y0
            observed=np.array([f@y[j*n:(j+1)*n] for j in range(4)])
            target=predicted_coefficients(t,k,lam,w)
            err=float(np.max(abs(observed-target)))
            max_error=max(max_error,err);n_cases+=1
            require(err<2e-11, f'Matrix/spectral agreement n={n},t={t},error={err}')
        for h in [-.3,.1,.4]:
            Q=full_generator(h,k,mu,H,g)
            pi=np.r_[1.,mu*np.exp(2*h)]/(1+np.exp(2*h))
            require(np.max(abs(pi@Q))<1e-12,'Finite-field stationarity')
            require(np.max(abs(pi[:,None]*Q-Q.T*pi[None,:]))<1e-12,'Finite-field detailed balance')
    # Piecewise-constant fields: full coefficient propagator versus kernel-mode ODE.
    k,mu,H,g=models[-1];B=generator_coefficients(k,mu,H,g);n=len(mu)+1
    lam,w=hidden_spectrum(mu,H,g);p0=np.r_[.5,.5*mu];f=np.r_[-1.,np.ones(len(mu))]
    y=np.zeros(4*n);y[:n]=p0
    small=np.zeros(3+len(lam)) # m1, base cubic, cubic correction, memory convolutions
    err_protocol=0.
    protocols=[(.4,.7),(.8,-.3),(.5,0.),(.9,1.1)]
    for duration,u in protocols:
        y=expm(duration*block_matrix(B,u))@y
        def rhs(_t:float,v:np.ndarray)->np.ndarray:
            m1,base,delta=v[:3];mem=v[3:]
            return np.r_[2*k*(u-m1),
                         -2*k*base+2*k*(u**3/6-m1*u*u/2),
                         -2*k*delta+k*w.sum()*u*u*(u-m1)-2*k*k*u*(w@mem),
                         -(k+lam)*mem+u*(u-m1)]
        sol=solve_ivp(rhs,(0.,duration),small,method='DOP853',rtol=2e-12,atol=2e-14)
        require(sol.success,'Reduced coefficient ODE integration')
        small=sol.y[:,-1]
        target=np.array([0.,small[0],0.,small[1]+small[2]])
        observed=np.array([f@y[j*n:(j+1)*n] for j in range(4)])
        err_protocol=max(err_protocol,float(np.max(abs(target-observed))))
        require(err_protocol<2e-10,'Arbitrary-protocol reduced memory check')
    # Direct finite-field matrix exponentials, compared to cubic approximation.
    k=1.;mu=np.array([.5,.5]);H=np.array([[-.25,.25],[.25,-.25]]);g=np.array([1.,-1.])
    lam,w=hidden_spectrum(mu,H,g);p0=np.array([.5,.25,.25]);f=np.array([-1.,1.,1.])
    coeff=predicted_coefficients(1.,k,lam,w);remainder=[]
    for h in [.1,.05,.025,.0125]:
        actual=float(p0@expm(full_generator(h,k,mu,H,g))@f)
        approx=h*coeff[1]+h**3*coeff[3]
        remainder.append({'field':h,'exact_mean':actual,'cubic_approximation':float(approx),
                          'absolute_error':abs(actual-approx),'error_over_h4':abs(actual-approx)/h**4})
    require(all(remainder[i+1]['absolute_error']<remainder[i]['absolute_error'] for i in range(3)),
            'Decreasing small-field remainder')
    return {'status':'PASS','matrix_spectral_comparisons':n_cases,
            'largest_coefficient_matrix_dimension':4*max(len(x[1])+1 for x in models),
            'max_matrix_spectral_absolute_error':max_error,
            'time_dependent_protocol_segments':len(protocols),
            'max_protocol_absolute_error':err_protocol,'state_count_examples':dimensions,
            'finite_field_remainder_at_t1':remainder}


def main()->None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('verification_report.json'))
    args=parser.parse_args()
    report={'status':'PASS','scope':'Deterministic checks; not independent proof review or novelty certification.',
            'versions':{'python':platform.python_version(),'numpy':np.__version__,
                        'scipy':scipy.__version__,'sympy':sp.__version__},
            'symbolic':symbolic_checks(),'deterministic':deterministic_checks()}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
