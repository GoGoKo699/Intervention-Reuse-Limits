"""Exact rational certificates for four- and five-state reversible models.

The rounded conductance fixture is fixed before verification. Floating-point
optimization discovered it, but this verifier uses only Fraction arithmetic.
No optimality or arbitrary-word error claim is made.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform

ROOT=Path(__file__).resolve().parents[1]
INPUT="reports/familiar_chain_accuracy.json"
INPUT_SHA256="7a51577858248c9a21ac5e2f41a005c83e2f9cf3c563b420d44a2b7b3fe06716"
PROOF="docs/FAMILIAR_CHAIN_PRECISION_FRONTIER.md"
PROOF_SHA256="ce62da3cbf368bc71a0829066d9c1c639bc7701402c701f12784b45ed21d0df6"

S=(1,1,1,-1,-1)
RHO=(F(1,6),F(1,12),F(1,4),F(1,6),F(1,3))
FIELDS=(F(0),F(1,2))
EDGES=tuple((i,j) for i in range(5) for j in range(i+1,5))
CONDUCTANCE_INTEGERS=(
 (2285376,0,7635089,3486189,1700907,0,2730914,3374977,4981230,1372514),
 (5909500,4929465,4211206,5786091,4916562,0,1803786,2897294,2439294,373412),
)
MENU=tuple((j,)*q for j in range(2) for q in range(1,5))+tuple(
 (j,)*a+(1-j,)*b for j in range(2) for a in (1,2) for b in (1,2))
ORDER=48
MODELS=(
 {'name':'four_state','S':(1,1,-1,-1),
  'rho':(F('0.33034911'),F('0.16965089'),F('0.16965089'),F('0.33034911')),
  'conductance_integers':((8706018,11080849,0,0,11080849,8706018),
                         (13064817,7178642,0,0,9927582,4354941)),
  'TV_upper':F(1,50000)},
 {'name':'five_state','S':S,'rho':RHO,
  'conductance_integers':CONDUCTANCE_INTEGERS,'TV_upper':F(9,2500000)},
)

def zeros(n):return [[F(0)for _ in range(n)]for _ in range(n)]
def identity(n):return [[F(i==j)for j in range(n)]for i in range(n)]
def matmul(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))for j in range(len(b[0]))]for i in range(len(a))]
def matvec(a,b):return [sum((x*y for x,y in zip(row,b)),F(0))for row in a]
def rowmat(b,a):return [sum((b[i]*a[i][j] for i in range(len(b))),F(0))for j in range(len(a[0]))]
def interval_exp_scalar(x):
 partial=sum((x**k/factorial(k) for k in range(ORDER+1)),F(0))
 first=x**(ORDER+1)/factorial(ORDER+1)
 tail=first/(1-x/(ORDER+2))
 assert 0<=x<ORDER+2
 return partial,partial+tail

def uniformized_exp(q,rate):
 """One-clock e^q; (q+rate*I)/rate is nonnegative substochastic."""
 n=len(q);eye=identity(n)
 h=[[q[i][j]/rate+eye[i][j]for j in range(n)]for i in range(n)]
 assert all(x>=0 for row in h for x in row)
 assert all(sum(row)<=1 for row in h)
 term=eye;partial=[row[:]for row in eye]
 for k in range(1,ORDER+1):
  term=[[x*rate/k for x in row]for row in matmul(term,h)]
  partial=[[partial[i][j]+term[i][j]for j in range(n)]for i in range(n)]
 expl,expu=interval_exp_scalar(rate);tail=expu-expl
 return ([[x/expu for x in row]for row in partial],
         [[(x+tail)/expl for x in row]for row in partial])

def target_generator(m):
 return [[F(-1),3*(1-m*m)/(9-m*m),F(0),8*m/(9-m*m)],
         [F(3,10),F(-1),F(3,10),F(0)],
         [F(0),F(1,3),F(-1),F(0)],
         [F(0),F(0),F(0),F(0)]]

def rival_generator(j,model):
 signs,rho0=model['S'],model['rho'];n=len(signs)
 edges=tuple((i,k)for i in range(n)for k in range(i+1,n))
 m=FIELDS[j];p=[rho*(1+m*s)for rho,s in zip(rho0,signs)]
 assert all(x>0 for x in p) and sum(p)==1
 q=zeros(n)
 for c,(a,b)in zip(model['conductance_integers'][j],edges):
  conductance=F(c,10**8)
  q[a][b]=conductance/p[a];q[b][a]=conductance/p[b]
 for i in range(n):q[i][i]=-sum(q[i])
 assert all(sum(row)==0 for row in q)
 assert all(p[i]*q[i][k]==p[k]*q[k][i]for i in range(n)for k in range(n))
 assert all(-q[i][i]<2 for i in range(n))
 # Every listed positive graph has a spanning tree rooted at zero.
 seen={0}
 while True:
  new=seen|{b for a in seen for b in range(n)if a!=b and q[a][b]>0}
  if new==seen:break
  seen=new
 assert len(seen)==n
 return q

def endpoint_target(word,kernels):
 u=[F(0),F(0),F(0),F(1)];v=[F(1),F(1,3),F(1,9),F(0)]
 ul,uu,vl,vu=u,u,v,v
 for j in word:
  lo,hi=kernels[j]
  ul,uu,vl,vu=matvec(lo,ul),matvec(hi,uu),matvec(lo,vl),matvec(hi,vu)
 return (ul[0],uu[0]),(vl[0],vu[0])

def endpoint_rival(word,kernels,model):
 signs,rho=model['S'],model['rho']
 conditioned=[]
 for sign in (1,-1):
  p=[2*p if s==sign else F(0)for p,s in zip(rho,signs)]
  assert sum(p)==1
  lo,hi=p,p
  for j in word:
   kl,ku=kernels[j]
   lo,hi=rowmat(lo,kl),rowmat(hi,ku)
  conditioned.append((sum(p for p,s in zip(lo,signs)if s==1)-sum(p for p,s in zip(hi,signs)if s==-1),
                      sum(p for p,s in zip(hi,signs)if s==1)-sum(p for p,s in zip(lo,signs)if s==-1)))
 plus,minus=conditioned
 u=((plus[0]+minus[0])/2,(plus[1]+minus[1])/2)
 v=((plus[0]-minus[1])/2,(plus[1]-minus[0])/2)
 return u,v

def absolute_interval(lo,hi):
 assert lo<=hi
 return (F(0)if lo<=0<=hi else min(abs(lo),abs(hi))),max(abs(lo),abs(hi))
def rounded(lo,hi):
 d=10**15
 return [str(F((lo*d).__floor__(),d)),str(F((hi*d).__ceil__(),d))]

def verify_model(model):
 signs,rho=model['S'],model['rho'];n=len(signs)
 edges=tuple((i,j)for i in range(n)for j in range(i+1,n))
 assert sum(rho)==1 and sum(p*s for p,s in zip(rho,signs))==0
 assert all(p>0 for p in rho)
 assert all(c>=0 for row in model['conductance_integers']for c in row)
 target=[uniformized_exp(target_generator(m),F(1))for m in FIELDS]
 rival=[uniformized_exp(rival_generator(j,model),F(2))for j in range(2)]
 assert len(MENU)==len(set(MENU))==16
 fixtures=[];maximum=[F(0),F(0)]
 for word in MENU:
  actual=endpoint_target(word,target);predicted=endpoint_rival(word,rival,model)
  error=[absolute_interval(x[0]-y[1],x[1]-y[0])for x,y in zip(actual,predicted)]
  tv=[max(e[k]for e in error)/2 for k in range(2)]
  assert tv[1]-tv[0]<F(1,10**25)
  assert tv[1]<model['TV_upper']
  if n==5:assert tv[1]<F(1,250000)
  maximum=[max(maximum[k],tv[k])for k in range(2)]
  fixtures.append({'word':list(word),'TV_interval':rounded(*tv)})
 return {'status':'PASS','arithmetic':'exact rational Fraction; fixed rounded fixture; no optimizer used',
  'states':n,'rho':[str(x)for x in rho],'readout':signs,'fields':[str(x)for x in FIELDS],
  'clock':'1','conductance_denominator':10**8,'edges':edges,'conductance_integers':model['conductance_integers'],
  'rate_uniformization':'2','series_degree':ORDER,'maximum_TV_interval':rounded(*maximum),
  'certified_TV_upper':str(model['TV_upper']),'fixtures':fixtures,
  'coarser_TV_upper':str(F(1,250000) if n==5 else model['TV_upper']),
  'scope':'The sixteen specified endpoint-pair settings only; one equilibrium preparation and deterministic readout; ordinary reversible continuous-time generators at both fields',
  'limitations':'No optimizer convergence, approximation optimality, full-path matching, or arbitrary-word tolerance is claimed.'}

def provenance():
 payload=(ROOT/INPUT).read_bytes()
 assert hashlib.sha256(payload).hexdigest()==INPUT_SHA256
 inherited=json.loads(payload);assert inherited['status']=='PASS'
 sources=dict(inherited['source_sha256'])
 proofs=dict(inherited['proof_snapshot_sha256'])
 reports=dict(inherited['input_report_sha256']);reports[INPUT]=INPUT_SHA256
 for name,digest in sources.items():
  assert hashlib.sha256((ROOT/'scripts'/name).read_bytes()).hexdigest()==digest
 for name,digest in {**proofs,**reports}.items():
  assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
 assert hashlib.sha256((ROOT/PROOF).read_bytes()).hexdigest()==PROOF_SHA256
 sources[Path(__file__).name]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
 proofs[PROOF]=PROOF_SHA256
 return sources,proofs,reports

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
 if args.output.resolve()==Path(__file__).resolve():raise ValueError('Output must not overwrite source')
 sources,proofs,reports=provenance()
 certificates={model['name']:verify_model(model)for model in MODELS}
 report={'status':'PASS','versions':{'python':platform.python_version()},
  'arithmetic':'Exact Fraction rational arithmetic, positive uniformization series, and geometric remainders; fixed coefficients only',
  'discovery':'Small local least-squares and minimax searches located the fixtures. Their numerical outcomes and optimizer termination flags are not verification evidence or optimality claims.',
  'scope':'Same sixteen initial/final pair experiments; tilts 0 and1/2, clock1; no all-word or full-path error bound',
  'common_interface':'One stationary zero-field preparation and deterministic binary readout. At each field the CTMC satisfies ordinary detailed balance under rho_m=rho_0*(1+m*S).',
  'models':certificates,'source_sha256':sources,'proof_snapshot_sha256':proofs,'input_report_sha256':reports}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(f'PASS: four-/five-state rational CTMC fixtures, 32 setting certificates -> {args.output}')
