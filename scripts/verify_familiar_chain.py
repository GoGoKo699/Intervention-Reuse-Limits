#!/usr/bin/env python3
"""Exact certificates for controlled compression of open heat-bath chains.

The all-length, positivity and accuracy statements are proved in the bound
proof snapshots. Exact finite checks complement those analytical arguments.
No optimizer, simulated observations or floating-point dynamics is used.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {'reports/switch_control_scope.json': '93d74f9c605fbfcc69a70f825b722cc67f1ce39fd3aee4b4d4f460f792f0ac7d'}
PROOFS = {'docs/FAMILIAR_CHAIN_POSITIVE_REALIZATION.md': '147f11bff41c9cbc7ecb5a60ea4cf7d935fe3ee8eff22dc1a61ddcc73aca26c8', 'docs/FAMILIAR_CHAIN_REVERSIBLE_BOUND.md': '2f2e7bb12b266e8ca70ed200995c084e85625d421c0bf0875632cc873e429659', 'docs/FAMILIAR_CHAIN_SIX_STATE_REALIZATION.md': 'ef06ad85440f7d0f0e5a817f1172d039dc626e8f8291b7a372384cb4a7000983', 'docs/FAMILIAR_CHAIN_PASSIVE_REALIZATION.md': 'd5cbf5b8c0a1ea537b09223b3abb2e03abd7cf50c959f4500f1ff55887b67741'}


def provenance():
    sources, proofs, count = {}, {}, 0
    for name, expected in INPUTS.items():
        payload = (ROOT/name).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == expected, name
        inherited = json.loads(payload)
        assert inherited['status'] == 'PASS'
        count += 2
        for source, digest in inherited['source_sha256'].items():
            assert hashlib.sha256((ROOT/'scripts'/source).read_bytes()).hexdigest() == digest, source
            sources[source] = digest
            count += 1
        for path, digest in inherited['proof_snapshot_sha256'].items():
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
            proofs[path] = digest
            count += 1
        for path, digest in inherited.get('input_report_sha256', {}).items():
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
            count += 1
    for path, digest in PROOFS.items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path
        proofs[path] = digest
        count += 1
    sources[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return sources, proofs, count


def positive_checks():
    t, m = sp.symbols("t m", positive=True)
    checks = []

    def zero(expr, label):
        value = sp.cancel(expr)
        if value != 0:
            raise AssertionError((label, value))
        checks.append(label)

    def matrix_zero(mat, label):
        for i in range(mat.rows):
            for j in range(mat.cols):
                zero(mat[i, j], f"{label}:{i},{j}")

    def model(n):
        den = 1-t*t*m*m
        A = m*(1-t*t)/den
        B = t*(1-m*m)/den
        L = (1-t*t)*(1+m)/(2*den)
        lam = (1-m)*(1-t*t*(3+2*m))/(2*den)
        a = 1/(2*(1+t*t))
        b = 2*t*t/(1+t*t)
        c = 3*t*t/(2*(1+t*t))
        d = (1-2*t*t)/(2*(1+t*t))
        R = sp.Matrix([[1]+[(2**(j+1)-1)*t**j if j<ell else -t**j
                             for j in range(n)] for ell in range(n+1)])
        Q = sp.zeros(n+1)
        Q[0,1] += L
        Q[1,0] += 1-L
        for ell in range(2,n+1):
            Q[ell,0] += lam
            Q[ell,1] += d-lam
        for ell in range(2,n):
            Q[ell,ell-1] += b
        for ell in range(1,n-1):
            Q[ell,ell+1] += a
        Q[n-1,n] += sp.Rational(1,2)
        Q[n,n-1] += c
        for ell in range(n+1):
            Q[ell,ell] = -sum(Q[ell,j] for j in range(n+1) if j!=ell)
        M = sp.zeros(n+1)
        M[0,1] = A
        M[1,1] = -1
        M[2,1] = B
        interior = t/(1+t*t)
        for j in range(1,n-1):
            M[j,j+1] = interior
            M[j+1,j+1] = -1
            M[j+2,j+1] = interior
        M[n-1,n] = t
        M[n,n] = -1
        nu = sp.Matrix([[sp.Rational(1,2)]+[sp.Rational(1,2**(ell+1))
                        for ell in range(1,n)]+[sp.Rational(1,2**n)]])
        return Q, R, M, nu

    den = 1-t*t*m*m
    L = (1-t*t)*(1+m)/(2*den)
    lam = (1-m)*(1-t*t*(3+2*m))/(2*den)
    lam0 = (1-3*t*t)/2
    d = (1-2*t*t)/(2*(1+t*t))
    zero(1-L-(1-m)*(1+t*t+2*t*t*m)/(2*den), "sign:1-L")
    zero(lam0-lam-m*(1-t*t)*(1-3*t*t*m)/(2*den), "sign:lambda-difference")
    zero(d-lam0-3*t**4/(2*(1+t*t)), "sign:reset-surplus")
    zero(L-(1-t*t)/2-m*(1-t*t)*(1+t*t*m)/(2*den), "sign:L-increase")
    # The two universal upper-bound remainders factor with 1-5t^2.
    row_one_zero = (1+t*t)/2+1/(2*(1+t*t))
    zero(sp.Rational(61,60)-row_one_zero
         -(1-5*t*t)*(1+6*t*t)/(60*(1+t*t)), "exit-cap:row-one")
    penultimate = (2+3*t*t)/(2*(1+t*t))
    zero(sp.Rational(13,12)-penultimate
         -(1-5*t*t)/(12*(1+t*t)), "exit-cap:penultimate")

    lengths = []
    for n in range(3,9):
        Q,R,M,nu = model(n)
        matrix_zero(Q*R-R*M, f"n={n}:intertwining")
        matrix_zero(Q*sp.ones(n+1,1), f"n={n}:row-sum")
        matrix_zero(nu*R-sp.Matrix([[1]+[0]*n]), f"n={n}:initial-means")
        D = sp.diag(*list(R[:,1]))
        matrix_zero(nu*D*R-sp.Matrix([[0]+[t**j for j in range(n)]]),
                    f"n={n}:initial-sign-cross-moments")
        tilted = nu*(sp.eye(n+1)+m*D)
        matrix_zero(tilted*Q, f"n={n}:tilted-stationarity")
        zero(sum(tilted)-1, f"n={n}:tilted-normalization")
        zero(Q[0,n], f"n={n}:missing-reverse-edge")
        zero(Q[n,0]-lam, f"n={n}:irreversible-edge")
        exit_expected = [L,1-L+1/(2*(1+t*t))]+[sp.Integer(1)]*(n-3) \
            +[(2+3*t*t)/(2*(1+t*t)),sp.Rational(1,2)]
        for ell in range(n+1):
            zero(-Q[ell,ell]-exit_expected[ell], f"n={n}:exit-rate:{ell}")
        # Consecutive row differences produce a diagonal coordinate matrix.
        differences = sp.Matrix([[R[i+1,j+1]-R[i,j+1] for j in range(n)]
                                 for i in range(n)])
        matrix_zero(differences-sp.diag(*[2**(j+1)*t**j for j in range(n)]),
                    f"n={n}:simplex-nondegeneracy")
        # Independently construct barycentric derivative entries.
        drift = R*M
        Qb = sp.zeros(n+1)
        for ell in range(n+1):
            g = [drift[ell,j+1]/(2**(j+1)*t**j) for j in range(n)]
            Qb[ell,0] = -g[0]
            for j in range(1,n):
                Qb[ell,j] = g[j-1]-g[j]
            Qb[ell,n] = g[n-1]
        matrix_zero(Q-Qb, f"n={n}:barycentric-rates")
        T = M[1:,1:].subs(m,0)
        seed = sp.eye(n)[:,0]
        columns = [seed]
        for k in range(1,n):
            columns.append(T*columns[-1])
        C = sp.Matrix.hstack(*columns)
        expected = t**(n-1)*(t/(1+t*t))**((n-1)*(n-2)//2)
        # This Krylov matrix is triangular; verify that fact and its diagonal product.
        for i in range(n):
            for j in range(i):
                zero(C[i,j], f"n={n}:krylov-triangular:{i},{j}")
        zero(sp.prod(C[i,i] for i in range(n))-expected, f"n={n}:cyclicity")
        lengths.append(n)

    # Exact rational and algebraic positivity fixtures include the coupling boundary.
    fixture_counts = []
    for n, tv, mv in [(3,sp.Rational(1,3),sp.Rational(2,3)),
                       (5,sp.Rational(1,4),sp.Rational(7,8)),
                       (8,sp.sqrt(5)/5,sp.Rational(9,10)),
                       (3,sp.sqrt(5)/5,sp.Integer(1))]:
        Q,R,M,nu = model(n)
        concrete = Q.subs({t:tv,m:mv}).applyfunc(sp.simplify)
        checked = 0
        for i in range(n+1):
            for j in range(n+1):
                if i!=j:
                    if concrete[i,j].is_nonnegative is not True:
                        raise AssertionError((n,tv,mv,i,j,concrete[i,j]))
                    checked += 1
        checks.append(f"n={n}:positive-fixture:t={tv}:m={mv}")
        fixture_counts.append({"n":n,"t":str(tv),"m":str(mv),"offdiagonals":checked})

    report = {
        "status":"PASS",
        "scope":"Exact algebraic fixtures complement, and do not replace, the all-length proof.",
        "symbolic_lengths": lengths,
        "exact_identity_checks":len(checks),
        "positivity_fixtures":fixture_counts,
        "largest_matrix":9,
        "floating_point_used":False,
        "theorem_domain":"n>=3, 0<t<=1/sqrt(5), 0<=m<1",
        "construction_state_count":"n+1",
        "claims_not_established":["optimal coupling boundary","hardware feasibility","dissipation advantage"]
    }

    return report


def six_state_checks():
    s=sp
    m=s.symbols('m',real=True)
    X=s.Matrix([[1,-1,-s.Rational(1,3)],[1,1,-s.Rational(5,3)],[1,1,1],[-1,1,s.Rational(1,3)],[-1,-1,s.Rational(5,3)],[-1,-1,-1]])
    rho0=s.Matrix([[s.Rational(1,6),s.Rational(1,12),s.Rational(1,4)]*2])
    rho=s.Matrix([[rho0[i]*(1+m*X[i,0]) for i in range(6)]])
    C=s.zeros(6)
    entries={
    (0,1):(1+m)*(1+2*m)/(15*(3+m)),
    (0,2):m/10,
    (0,3):(1-m)*(7+4*m)/(30*(3+m)),
    (0,4):m*(1-m)*(1+m)/(6*(3-m)*(3+m)),
    (0,5):(1-m)*(1+3*m)/(10*(3-m)),
    (1,2):(1+m)*(1+2*m)/(20*(3+m)),
    (1,4):(1-m)*(1+m)/(12*(3+m)),
    (2,3):(1-m)*(1+2*m)/(10*(3+m)),
    (2,5):(1-m)/20,
    (3,4):(1-m)*(2-m)/(30*(3+m)),
    (4,5):(1-m)*(1-2*m)/(20*(3-m)),
    }
    for (i,j),c in entries.items(): C[i,j]=C[j,i]=c
    Q=s.Matrix(6,6,lambda i,j:C[i,j]/rho[i] if i!=j else 0)
    for i in range(6):Q[i,i]=-sum(Q[i,j]for j in range(6)if i!=j)
    A=8*m/(9-m*m);B=3*(1-m*m)/(9-m*m)
    D=s.Matrix([[A-X[i,0]+B*X[i,1],s.Rational(3,10)*(X[i,0]+X[i,2])-X[i,1],X[i,1]/3-X[i,2]]for i in range(6)])
    checks=0
    def zero(Z):
     nonlocal checks
     for v in Z:
      assert s.cancel(v)==0,v
      checks+=1
    zero(Q*X-D)
    zero(s.diag(*rho)*Q-Q.T*s.diag(*rho))
    zero(rho*Q)
    zero(rho0*X)
    zero(s.Matrix([[sum(rho0)-1,sum(rho)-1]]))
    R=s.Matrix(3,3,lambda i,j:s.Rational(1,3)**abs(i-j))
    zero(X.T*s.diag(*rho0)*X-R)
    for sign in [-1,1]:
     conditional=s.zeros(1,3)
     for i in range(6):
      if X[i,0]==sign:conditional+=2*rho0[i]*X[i,:]
     zero(conditional-s.Matrix([[sign,sign*s.Rational(1,3),sign*s.Rational(1,9)]]))

    # Independent exact exit-cap identities and endpoint sign fixtures.
    remainders=[
     (12*m**3+19*m*m-8*m+9)/(5*(3-m)*(1+m)*(3+m)),
     (3-4*m)/(5*(m+3)),
     (6*m*m+11*m+9)/(5*(m+1)*(m+3)),
     (3-4*m)/(5*(m+3)),
     (9+5*m-6*m*m)/(5*(9-m*m)),
     (9-8*m)/(5*(3-m))]
    zero(s.Matrix([1+Q[i,i]-remainders[i] for i in range(6)]))
    for field in (s.S(0),s.Rational(1,2)):
        assert all(s.simplify(v.subs(m,field))>=0 for v in entries.values())
        assert all(s.simplify(v.subs(m,field))>0 for v in rho)
        checks += 2
    return {'status':'PASS','exact_checks':checks,'states':6,
            'coupling':'1/3','tilt_interval':['0','1/2'],
            'exit_rate_bound':'strictly below 1',
            'scope':'Symbolic closure, detailed balance, full stationary Gram and conditional preparation; factor signs in the proof establish interval positivity.'}


def gram_checks():
    checks=[]
    def check(name, value):
        if value is not True and value != sp.true:
            raise AssertionError(name + ': ' + str(value))
        checks.append(name)
    def eq(name, left, right):
        if isinstance(left, sp.MatrixBase) or isinstance(right, sp.MatrixBase):
            z=sp.Matrix(left)-sp.Matrix(right)
            check(name, all(sp.simplify(v)==0 for v in z))
        else:
            check(name, sp.simplify(left-right)==0)
    def simp(M):
        return M.applyfunc(sp.simplify)

    n=3
    t=sp.sqrt(7)/7
    a=sp.sqrt(7)/8
    fields=[sp.S(0),sp.sqrt(sp.Rational(133,319)),sp.sqrt(3)/2]
    kappas=[sp.Rational(1,2),sp.Rational(9,20),sp.Rational(2,5)]
    C=sp.Matrix([[t**abs(i-j) for j in range(3)] for i in range(3)])
    T=sp.Matrix([1,t,t*t])
    G0=sp.diag(1,C)
    Gs=sp.zeros(4)
    Gs[0,1:4]=T.T
    Gs[1:4,0]=T
    p=sp.Matrix([[1,0,0,0]])
    c=sp.Matrix([[0,1,t,t*t]])
    e0=sp.eye(4)[:,0]
    e1=sp.eye(4)[:,1]
    Ms=[]; Es=[]; Bs=[]; Hs=[]; Gs_field=[]
    for idx,(m,kappa) in enumerate(zip(fields,kappas)):
        A=sp.simplify(m*(1-t*t)/(1-t*t*m*m))
        B=sp.simplify(t*(1-m*m)/(1-t*t*m*m))
        M=sp.Matrix([[0,A,0,0],[0,-1,a,0],[0,B,-1,t],[0,0,a,-1]])
        G=G0+m*Gs
        eq(f'field_{idx}_stationary', (p+m*c)*M, sp.zeros(1,4))
        eq(f'field_{idx}_detailed_balance_mean', G*M, M.T*G)
        eq(f'field_{idx}_kappa',a*(B+t),kappa*kappa)
        eigs=[sp.S(0),sp.S(-1),-1+kappa,-1-kappa]
        vals=[sp.S(1),sp.Rational(1,2**20),sp.S(2)**(-20+20*kappa),sp.S(2)**(-20-20*kappa)]
        E=sp.zeros(4)
        projs=[]
        for j,lam in enumerate(eigs):
            P=sp.eye(4)
            for k,mu in enumerate(eigs):
                if j!=k:
                    P=P*(M-mu*sp.eye(4))/(lam-mu)
            P=simp(P)
            eq(f'field_{idx}_projector_{j}_eigen',M*P,lam*P)
            eq(f'field_{idx}_projector_{j}_square',P*P,P)
            projs.append(P)
            E+=vals[j]*P
        E=simp(E)
        eq(f'field_{idx}_projector_sum',sum(projs,sp.zeros(4)),sp.eye(4))
        eq(f'field_{idx}_propagator_constant',E*e0,e0)
        eq(f'field_{idx}_propagator_balance',G*E,E.T*G)
        H=sp.Matrix.hstack(e0,e1,E*e1,E*E*e1)
        H=simp(H)
        check(f'field_{idx}_cyclic',sp.simplify(H.det())!=0)
        inv=simp(H.inv())
        eq(f'field_{idx}_basis_inverse',H*inv,sp.eye(4))
        Ms.append(M); Es.append(E); Bs.append(inv); Hs.append(H); Gs_field.append(G)

    menu={tuple([j]*q) for j in range(3) for q in range(1,5)}
    menu|={tuple([j]*aa+[1]*bb) for j in (0,2) for aa in range(1,3) for bb in range(1,3)}
    check('menu_twenty',len(menu)==20)
    check('menu_max_four_ticks',max(map(len,menu))==4)
    check('menu_max_two_segments',max(1+sum(x!=y for x,y in zip(w,w[1:])) for w in menu)==2)
    # All data are obtained by exactly the declared endpoint menu.
    data={}
    for word in sorted(menu):
        E=sp.eye(4)
        for j in word:
            E=E*Es[j]
        mean=sp.simplify((p*E*e1)[0])
        corr=sp.simplify((c*E*e1)[0])
        data[word]=(mean,corr)

    def endpoint(word):
        if not word:
            return sp.S(0),sp.S(1)
        return data[tuple(word)]

    def entry(j,k,aa,bb):
        """<H_j[aa],H_k[bb]> under pi_j, using endpoint data."""
        m=fields[j]
        if aa==0 and bb==0:
            return sp.S(1)
        if aa==0:
            mean,corr=endpoint([k]*(bb-1))
            return mean+m*corr
        if bb==0:
            return m
        mean,corr=endpoint([j]*(aa-1)+[k]*(bb-1))
        return corr+m*mean

    for j in range(3):
        A=sp.Matrix([[entry(j,j,aa,bb) for bb in range(4)] for aa in range(4)])
        eq(f'field_{j}_own_gram_from_menu',Bs[j].T*A*Bs[j],Gs_field[j])
    for j in (0,2):
        A=sp.Matrix([[entry(j,1,aa,bb) for bb in range(4)] for aa in range(4)])
        eq(f'field_{j}_mixed_gram_from_menu',Bs[j].T*A*Bs[1],Gs_field[j])
        # In contrast with the previous Gram checks, the data-rank factorization
        # only uses target reversibility, and is valid for arbitrary rival kernels.
        rows=sp.Matrix.vstack(p+fields[j]*c,*[(c+fields[j]*p)*(Es[j]**k) for k in range(3)])
        D=rows*Hs[j]
        eq(f'field_{j}_general_data_rank_gram',Bs[j].T*D*Bs[j],Gs_field[j])
        check(f'field_{j}_general_data_rank_four',sp.simplify(D.det())!=0)

    mL,mM,mR=fields
    wL=sp.simplify((mR-mM)/(mR-mL)); wR=1-wL
    check('positive_interpolation_weights', bool(wL>0) and bool(wR>0))
    eq('affine_gram_identity',Gs_field[1],wL*Gs_field[0]+wR*Gs_field[2])
    for sign in (1,-1):
        sector=G0+sign*Gs
        eq(f'sector_{sign}_interpolation',((mR-sign)*Gs_field[0]+(sign-mL)*Gs_field[2])/(mR-mL),sector)
        check(f'sector_{sign}_rank_three',sector.rank()==3)
        red=sector.extract([0,2,3],[0,2,3])
        for k in range(1,4):
            check(f'sector_{sign}_minor_{k}_positive',bool(sp.simplify(red[:k,:k].det())>0))
        signmat=sp.diag(1,sign,sign)
        eq(f'sector_{sign}_conditional_covariance',red,signmat*C*signmat)

    # Universal robust norm constants: nonnegative residuals, exact affine
    # interpolation, and a bilinear l1 coefficient estimate are proved in text.
    uL,uM,uR,ep,KK=sp.symbols('uL uM uR ep KK',positive=True)
    wl,wr=sp.symbols('wl wr',positive=True)
    eq('tv_residual_bound_coefficient',ep*KK**2+(wl+wr)*(2*ep*KK**2+ep*KK**2),ep*KK**2*(1+3*(wl+wr)))
    eq('tv_residual_when_weights_sum_one',(1+3*(wl+wr)).subs(wr,1-wl),4)
    for sign in (1,-1):
        outer=sp.simplify((abs(mR-sign)+abs(sign-mL))/(mR-mL))
        explicit=sp.simplify((2-sign*(mL+mR))/(mR-mL))
        eq(f'tv_sector_{sign}_extrapolation',outer,explicit)

    # Exact AR(1) precision check provides a simple eigenvalue lower bound for
    # the target conditional Gram, valid at every chain length.
    z=sp.symbols('z',positive=True)
    for size in range(2,9):
        R=sp.Matrix([[z**abs(i-j) for j in range(size)] for i in range(size)])
        precision=sp.zeros(size)
        for i in range(size):
            precision[i,i]=1 if i in (0,size-1) else 1+z*z
        for i in range(size-1):
            precision[i,i+1]=precision[i+1,i]=-z
        eq(f'conditional_precision_size_{size}',R*precision,(1-z*z)*sp.eye(size))
        menu_size=3*(2*size-2)+2*(size-1)**2
        check(f'menu_count_size_{size}',menu_size==2*(size-1)*(size+2))

    report={
      'status':'PASS',
      'exact_checks':len(checks),
      'fixture':{'n':3,'t':'1/sqrt(7)','m':['0','sqrt(133/319)','sqrt(3)/2'],'clock':'20*log(2)','clock_kind':'exact CTMC clock','settings':20,'maximum_ticks':4,'maximum_segments':2},
      'largest_matrix':8,
      'no_optimization_or_simulation':True,
      'scope':'Exact projector/mean-basis and finite endpoint-Gram identities; theorem uses analytic positivity and norm arguments.',
      'checks':checks,
    }
    return report


def passive_checks():

    checks=0
    def eq(a,b):
        nonlocal checks
        vals=a-b if isinstance(a,sp.MatrixBase) else [a-b]
        assert all(sp.simplify(v)==0 for v in vals)
        checks+=1
    t=sp.Rational(1,3)
    T=sp.Matrix([[-1,sp.Rational(3,10),0],[t,-1,t],[0,sp.Rational(3,10),-1]])
    cross=sp.Matrix([[1,t,t*t]])
    seed=sp.Matrix([1,0,0])
    mom=[sp.S(1)]+[sp.simplify((cross*((-T)**k)*seed)[0]/2) for k in range(1,8)]
    x=sp.symbols('x')
    def inner(a,b):
        poly=sp.Poly(sp.expand(a*b),x)
        return sp.simplify(sum(coef*mom[powr[0]] for powr,coef in poly.terms()))
    polys=[]
    for k in range(4):
        poly=x**k
        for old in polys:
            poly-=inner(old,poly)*old
        norm=inner(poly,poly)
        assert norm>0
        checks+=1
        polys.append(sp.simplify(poly/sp.sqrt(norm)))
    J=sp.Matrix(4,4,lambda i,j:inner(polys[i],x*polys[j]))
    D=sp.diag(1,-1,1,-1)
    L=D*J*D
    v=L.nullspace()[0]
    if v[0]<0:v=-v
    v=sp.simplify(v/sp.sqrt((v.T*v)[0]))
    assert all(z>0 for z in v)
    checks+=1
    V=sp.diag(*v)
    Q=(-V.inv()*L*V).applyfunc(sp.simplify)
    rho=sp.Matrix([[z*z for z in v]])
    S=sp.Matrix([-1,1,1,1])
    eq(Q*sp.ones(4,1),sp.zeros(4,1))
    eq(sp.diag(*rho)*Q,Q.T*sp.diag(*rho))
    eq(rho[0],sp.Rational(1,2))
    eq((rho*S)[0],0)
    assert all(Q[i,j]>=0 for i in range(4) for j in range(4) if i!=j)
    checks+=1
    for k in range(8):
        eq((rho*sp.diag(*S)*(Q**k)*S)[0],(cross*(T**k)*seed)[0])
    return {'status':'PASS','exact_checks':checks,'physical_spins':3,
            'reversible_states':4,'construction':'Inverse Jacobi matrix and positive ground-vector transformation',
            'moment_orders_checked':list(range(8)),
            'scope':'Exact finite fixture; the standard spectral-measure proof establishes all passive pair laws.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert args.output.resolve() != Path(__file__).resolve()
    sources, proofs, provenance_checks = provenance()
    positive = positive_checks()
    six = six_state_checks()
    gram = gram_checks()
    passive = passive_checks()
    count = (provenance_checks + positive['exact_identity_checks']
             + six['exact_checks'] + gram['exact_checks'] + passive['exact_checks'])
    report = {
        'status':'PASS','checks':count,'largest_matrix_dimension':9,
        'versions':{'python':platform.python_version(),'sympy':sp.__version__},
        'arithmetic':'Exact symbolic, rational and algebraic identities; no floating point, optimization or simulated observations',
        'positive_realization':positive,'finite_three_field_gram':gram,
        'sharp_six_state_realization':six,'passive_birth_death':passive,
        'source_sha256':sources,'proof_snapshot_sha256':proofs,
        'input_report_sha256':INPUTS,
        'limitations':'Finite fixtures complement the analytical all-length proofs. The TV radius is parameter dependent, with no uniform-in-length or practical trial guarantee. No device, dissipation, physical-bit savings, full-path equality or priority certification is established.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(f'PASS: {count} exact familiar-chain checks -> {args.output}')


if __name__ == '__main__':
    main()
