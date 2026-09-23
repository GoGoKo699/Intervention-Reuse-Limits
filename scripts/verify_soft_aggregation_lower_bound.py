#!/usr/bin/env python3
"""Exact bounded checks for randomized Bayes aggregation and its joint lift.

A four-state hidden example has overlapping color-preserving encoder rows.
Its joint lift has eight hidden states and nine physical states. A 27 by 27
auxiliary path matrix checks the Ritz identity; it is not a retained model.
No growing dictionary or trajectory simulation is constructed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from fractions import Fraction as F
from pathlib import Path

import sympy as sp

Q = sp.Rational


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def physical_generator(hidden: sp.Matrix, mu: sp.Matrix, g: list, base: sp.Expr) -> tuple[sp.Matrix, sp.Matrix]:
    """Use h=2 log(base) and sensitivities +/-1/2, so all entries are rational."""
    size = len(g)+1
    full = sp.zeros(size)
    full[1:, 1:] = hidden
    for i, sensitivity in enumerate(g, 1):
        full[0, i] = mu[i-1]*base**int(2*(1+sensitivity))
        full[i, 0] = base**int(2*(sensitivity-1))
        full[0, 0] -= full[0, i]
        full[i, i] -= full[i, 0]
    pi = sp.Matrix([[1]+[base**4*value for value in mu]])/(1+base**4)
    require(full*sp.ones(size, 1) == sp.zeros(size, 1), 'Physical generator row sums')
    require(pi*full == sp.zeros(1, size), 'Physical stationary law')
    require(sp.diag(*pi)*full == full.T*sp.diag(*pi), 'Exact field-by-field physical detailed balance')
    return full, pi


def model_checks() -> tuple[dict, dict]:
    mu = sp.ones(1, 4)/4
    g = [-Q(1, 2), -Q(1, 2), Q(1, 2), Q(1, 2)]
    averaging = sp.ones(4, 1)*mu
    local = sp.zeros(4)
    local[0, 2] = local[2, 0] = Q(1, 4)
    local[0, 0] = local[2, 2] = -Q(1, 4)
    k = Q(3, 2)*(averaging-sp.eye(4))+local
    nu = Q(5, 2)
    p = sp.eye(4)+k/nu
    a = sp.diag(sp.Matrix([[Q(3, 4), Q(1, 4)], [Q(1, 4), Q(3, 4)]]),
                sp.Matrix([[Q(3, 4), Q(1, 4)], [Q(1, 4), Q(3, 4)]]))
    muhat = mu*a
    bayes = sp.diag(*muhat).inv()*a.T*sp.diag(*mu)
    require(a*sp.ones(4, 1) == sp.ones(4, 1) and bayes*sp.ones(4, 1) == sp.ones(4, 1),
            'Encoder and Bayes reverse channel are stochastic')
    require(all(sum(1 for c in range(4) if a[z, c] > 0) == 2 for z in range(4)),
            'Every encoder row genuinely overlaps two retained labels')
    require(all(a[z, c] == 0 or g[z] == g[c] for z in range(4) for c in range(4)),
            'The encoder exactly preserves each actuator color')
    phat = bayes*p*a
    khat = nu*(phat-sp.eye(4))
    bka = bayes*k*a
    require(khat == bka+nu*(bayes*a-sp.eye(4)) and khat != bka,
            'Uniformized Bayes dynamics contain the nonzero resampling term')
    negative = [(i, j, bka[i, j]) for i in range(4) for j in range(4) if i != j and bka[i, j] < 0]
    require(len(negative) > 0, 'In this example BKA has a negative off-diagonal and is not a Markov generator')
    require(phat*sp.ones(4, 1) == sp.ones(4, 1) and all(value >= 0 for value in phat),
            'BPA is an actual stochastic transition matrix')
    require(sp.diag(*muhat)*phat == phat.T*sp.diag(*muhat), 'Exact Bayes aggregate reversibility')
    require(k.eigenvals() == {sp.Integer(0): 1, -Q(3, 2): 2, sp.Integer(-2): 1},
            'Target hidden spectrum lies in the required interval')
    require(all(value == 0 or -nu <= value <= -Q(3, 2) for value in khat.eigenvals()),
            'Aggregate hidden spectrum preserves the interval [3/2,5/2]')

    joint = [(z, c) for z in range(4) for c in range(4) if a[z, c] > 0]
    muj = sp.Matrix([[mu[z]*a[z, c] for z, c in joint]])
    jmap = sp.Matrix([[int(z == original) for original in range(4)] for z, _ in joint])
    jstar = sp.diag(*mu).inv()*jmap.T*sp.diag(*muj)
    require(jstar*jmap == sp.eye(4), 'The original-state lift is an isometry in stationary weights')
    pj = jmap*p*jstar
    kj = nu*(pj-sp.eye(8))
    require(pj == sp.Matrix([[p[z, zz]*a[zz, cc] for zz, cc in joint] for z, _ in joint]),
            'Joint kernel equals the claimed conditional-resampling formula')
    require(pj*sp.ones(8, 1) == sp.ones(8, 1) and all(value >= 0 for value in pj), 'Joint lift is stochastic')
    require(sp.diag(*muj)*pj == pj.T*sp.diag(*muj), 'Joint lift is ordinarily reversible')
    require(kj*jmap == jmap*k, 'Original hidden dynamics intertwine exactly')
    require(kj*(sp.eye(8)-jmap*jstar) == -nu*(sp.eye(8)-jmap*jstar),
            'Every extra orthogonal mode has exactly the uniformization relaxation rate')
    require(kj.eigenvals() == {sp.Integer(0): 1, -Q(3, 2): 2, sp.Integer(-2): 1, -nu: 4},
            'The joint spectrum consists of the target spectrum plus four extra modes')
    cell = sp.Matrix([[int(label == c) for c in range(4)] for _, label in joint])
    cellstar = sp.diag(*muhat).inv()*cell.T*sp.diag(*muj)
    require(cellstar*pj*cell == phat and cellstar*cell == sp.eye(4),
            'Ordinary partition of the joint lift gives exactly BPA')
    jf, cf = sp.diag(sp.ones(1), jmap), sp.diag(sp.ones(1), cell)
    pi0 = sp.Matrix([[Q(1, 2)]+[value/2 for value in muj]])
    pihat0 = sp.Matrix([[Q(1, 2)]+[value/2 for value in muhat]])
    cfstar = sp.diag(*pihat0).inv()*cf.T*sp.diag(*pi0)
    projection = cf*cfstar
    require(projection*projection == projection and sp.diag(*pi0)*projection == projection.T*sp.diag(*pi0),
            'Full physical conditional expectation is an orthogonal projection')
    fields, fulls = [], {}
    for base in (Q(1, 2), Q(1), Q(2)):
        original, original_pi = physical_generator(k, mu, g, base)
        lifted, lifted_pi = physical_generator(kj, muj, [g[z] for z, _ in joint], base)
        aggregate, aggregate_pi = physical_generator(khat, muhat, g, base)
        require(lifted*jf == jf*original and lifted_pi*jf == original_pi,
                'Full physical controlled generator and preparation intertwine')
        require(cfstar*lifted*cf == aggregate, 'Full physical stationary-flux partition equals the Bayes aggregate')
        original_readout, lifted_readout = sp.Matrix([-1]+[1]*4), sp.Matrix([-1]+[1]*8)
        require(jf*original_readout == lifted_readout, 'The fixed physical readout intertwines')
        if base == 1:
            for generator in (original, lifted, aggregate):
                count = generator.rows
                visible_lift = sp.zeros(count, 2)
                visible_lift[0, 0] = 1
                for i in range(1, count):
                    visible_lift[i, 1] = 1
                require(generator*visible_lift == visible_lift*sp.Matrix([[-1, 1], [1, -1]]),
                        'Every model has exact passive telegraph lumpability')
        fulls[base] = lifted
        fields.append({'exp_h_over_two_exact': str(base), 'physical_states': [5, 9, 5],
                       'detailed_balance': 'exact', 'controlled_intertwining': 'exact'})
    e = sp.Matrix([1]+[0]*8)
    feature = fulls[1]*fulls[2]*e
    lost = (sp.eye(9)-projection)*feature
    lost_norm = (lost.T*sp.diag(*pi0)*lost)[0]
    require(lost_norm > 0, 'A physical two-generator observable feature has genuinely nonzero reconstruction loss')
    return ({'hidden_target_states': 4, 'retained_hidden_labels': 4, 'joint_hidden_states': 8,
             'joint_physical_states': 9, 'nonzero_encoder_entries': 8,
             'actuator_histogram_exact': {'-1/2': '1/2', '1/2': '1/2'},
             'target_relaxation_spectrum_exact': {'0': 1, '3/2': 2, '2': 1},
             'joint_extra_relaxation_rate_exact': '5/2', 'joint_extra_modes': 4,
             'aggregate_relaxation_spectrum_exact': {str(-value): count for value, count in khat.eigenvals().items()},
             'negative_BKA_off_diagonals': [{'row': i, 'column': j, 'value_exact': str(value)} for i, j, value in negative],
             'physical_field_checks': fields, 'observable_squared_projection_loss_exact': str(lost_norm)},
            {'Q0': fulls[1], 'Qh': fulls[2], 'pi0': pi0, 'pihat0': pihat0,
             'cell': cf, 'cellstar': cfstar, 'E': projection, 'e': e, 'feature': feature})


def ritz_checks(model: dict) -> dict:
    weight, n = sp.diag(*model['pi0']), 9
    # Here H=2 log(2), G=1/2, Lambda=5/2. Thus exp(H)=4,
    # R=8 and the proof's bound B0=exp(H)*2*(Lambda+R)=84 is exact.
    b0 = 84
    letters = (model['Qh'], model['Q0'])
    path = sp.zeros(3*n)
    for step, operator in enumerate(letters, 1):
        adjoint = weight.inv()*operator.T*weight
        path[step*n:(step+1)*n, (step-1)*n:step*n] = operator/(2*b0)
        path[(step-1)*n:step*n, step*n:(step+1)*n] = adjoint/(2*b0)
    metric = sp.diag(weight, weight, weight)
    lift = sp.diag(model['cell'], model['cell'], model['cell'])
    reverse = sp.diag(model['cellstar'], model['cellstar'], model['cellstar'])
    projection = lift*reverse
    require(metric*path == path.T*metric, 'The physical generator path is self-adjoint in the exact weighted norm')
    compressed = reverse*path*lift
    require(lift*compressed*reverse == projection*path*projection,
            'The auxiliary compressed path is exactly the compression of the generator path')
    start = sp.zeros(27, 1)
    start[:9, :] = model['e']
    require(projection*start == start, 'The visible initial vector lies in the retained function space')
    shortest = (path*path*start)[18:27, :]
    require(shortest == model['feature']/(2*b0)**2,
            'The shortest clock path recovers the desired physical generator word')
    t = Q(1, 16)
    positive = sp.eye(27)-t*path
    full_solution = positive.inv()*start
    ritz_solution = lift*(sp.eye(15)-t*compressed).inv()*reverse*start
    error = full_solution-ritz_solution
    scalar_deficit = (start.T*metric*error)[0]
    energy = (error.T*metric*positive*error)[0]
    projected = (sp.eye(27)-projection)*full_solution
    squared_defect = (projected.T*metric*projected)[0]
    require(scalar_deficit == energy and scalar_deficit > 0,
            'The positive Ritz deficit equals the exact Galerkin error energy and is nonzero')
    require(squared_defect > 0 and scalar_deficit >= (1-t)*squared_defect,
            'The Ritz deficit controls the nonzero discarded resolvent component')
    return {'clock_sites': 3, 'physical_space_dimension': 9, 'auxiliary_matrix_dimension': 27,
            'compressed_auxiliary_dimension': 15, 'generator_norm_bound_exact': str(b0),
            'resolvent_parameter_exact': str(t), 'ritz_energy_identity': 'exact',
            'scalar_deficit_exact': str(scalar_deficit), 'discarded_resolvent_squared_norm_exact': str(squared_defect),
            'lower_bound_margin_exact': str(scalar_deficit-(1-t)*squared_defect),
            'scope': 'A rational finite-dimensional test of the proof identity. Clock coordinates are an algebraic device, not free physical states.'}


def budget_checks() -> dict:
    require(F(16, 15)**15 < 4, 'Exact rational certificate for h2(1/16)<3/8')
    budgets = []
    # Representative C=2, B=3, kappa=1/4 check only the allocation algebra.
    # These are not estimates of the theorem's field-interpolation constants.
    for n in (1, 2, 3, 4):
        r = 2**n
        delta_root = F(1, 96*r*4*3**(2*n+2))
        delta = delta_root**2
        per_feature = 4*3**(2*n+2)*delta_root
        root_mass = F(1, 6*r)
        conditional_total = r*per_feature/root_mass
        require(per_feature == F(1, 96*r) and conditional_total == F(r, 16),
                'Uniform squared feature loss yields the required conditional root distortion')
        budgets.append({'n': n, 'r': r, 'delta_exact': str(delta),
                        'per_feature_squared_loss_exact': str(per_feature),
                        'root_event_mass_exact': str(root_mass),
                        'conditional_summed_distortion_exact': str(conditional_total)})
    return {'entropy_certificate': '(16/15)^15 < 4', 'representative_budgets': budgets,
            'scope': 'Exact algebra at C=2, B=3, kappa=1/4; actual theorem constants remain symbolic and may be much larger.'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('reports/soft_aggregation_lower_bound.json'))
    args = parser.parse_args()
    physical, model = model_checks()
    report = {'status': 'PASS',
              'scope': 'Exact overlapping Bayes encoder, Markov joint lift, full physical intertwining, genuinely lost observable feature, positive Ritz energy identity, and representative reconstruction budgets.',
              'versions': {'python': platform.python_version(), 'sympy': sp.__version__},
              'bayes_and_physical_lift': physical, 'auxiliary_ritz_identity': ritz_checks(model),
              'entropy_and_budgets': budget_checks(), 'largest_physical_state_count': 9,
              'largest_matrix_dimension': 27,
              'limitations': 'The four-state binary example checks general aggregation and observability identities; it is not the six-level asymptotic dictionary. The growing state lower bound and all-clock transfer are analytic arguments in the companion proofs, not conclusions from finite enumeration.',
              'provenance': 'Fresh verifier reconstructed after workspace recovery; no claim of byte identity with the inaccessible earlier script.',
              'source_sha256': {Path(__file__).name: hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
