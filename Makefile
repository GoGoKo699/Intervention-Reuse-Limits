PYTHON ?= python
export OPENBLAS_NUM_THREADS := 1
export OMP_NUM_THREADS := 1

.PHONY: check
check:
	$(PYTHON) scripts/check_repository.py
	mkdir -p .check-output
	$(PYTHON) scripts/verify_checkpoint.py --output .check-output/checkpoint.json
	$(PYTHON) scripts/verify_finite_accuracy.py --output .check-output/finite_accuracy.json
	$(PYTHON) scripts/verify_quadrature.py --output .check-output/quadrature.json
	$(PYTHON) scripts/verify_minimal_realization.py --output .check-output/minimal_realization.json
	$(PYTHON) scripts/verify_response_lower_bounds.py --output .check-output/response_lower_bounds.json
	$(PYTHON) scripts/verify_unrestricted_rate_lower_bound.py --output .check-output/unrestricted_rate_lower_bound.json
	$(PYTHON) scripts/verify_finite_field.py --output .check-output/finite_field.json
	$(PYTHON) scripts/verify_path_information.py --output .check-output/path_information.json
	$(PYTHON) scripts/verify_actuator_hierarchy.py --output .check-output/actuator_hierarchy.json
	$(PYTHON) scripts/verify_general_compression.py --output .check-output/general_compression.json
	$(PYTHON) scripts/verify_reversible_compression.py --output .check-output/reversible_compression.json
	$(PYTHON) scripts/verify_general_controlled_lower_bound.py --output .check-output/general_controlled_lower_bound.json
	$(PYTHON) scripts/verify_bounded_rate_prediction.py --output .check-output/bounded_rate_prediction.json
	$(PYTHON) scripts/verify_shift_register_lower_bound.py --output .check-output/shift_register_lower_bound.json
	$(PYTHON) scripts/verify_polynomial_controlled_lower_bound.py --output .check-output/polynomial_controlled_lower_bound.json
	$(PYTHON) scripts/verify_constant_step_compression.py --output .check-output/constant_step_compression.json
	$(PYTHON) scripts/verify_bounded_density_sampling.py --output .check-output/bounded_density_sampling.json
	$(PYTHON) scripts/verify_analytic_constant_step.py --output .check-output/analytic_constant_step.json
	$(PYTHON) scripts/verify_moment_density_sampling.py --output .check-output/moment_density_sampling.json
	$(PYTHON) scripts/verify_sparse_reversible_compression.py --output .check-output/sparse_reversible_compression.json
	$(PYTHON) scripts/verify_local_walk_lower_bound.py --output .check-output/local_walk_lower_bound.json
	$(PYTHON) scripts/verify_expander_scenery_compression.py --output .check-output/expander_scenery_compression.json
	$(PYTHON) scripts/verify_expander_scenery_lower_bound.py --output .check-output/expander_scenery_lower_bound.json
	$(PYTHON) scripts/verify_aggregation_state_lower_bound.py --output .check-output/aggregation_state_lower_bound.json
	$(PYTHON) scripts/verify_register_scenery_compression.py --output .check-output/register_scenery_compression.json
	$(PYTHON) scripts/verify_soft_aggregation_lower_bound.py --output .check-output/soft_aggregation_lower_bound.json
	$(PYTHON) scripts/verify_exact_reversible_prefix_obstruction.py --output .check-output/exact_reversible_prefix_obstruction.json
	$(PYTHON) scripts/verify_dynamic_lamp_reversibility_lower_bound.py --output .check-output/dynamic_lamp_reversibility_lower_bound.json
	$(PYTHON) scripts/verify_binary_reversibility_lower_bound.py --output .check-output/binary_reversibility_lower_bound.json
	$(PYTHON) scripts/verify_state_speed_boundary.py --output .check-output/state_speed_boundary.json
	$(PYTHON) scripts/verify_uncapped_observability.py --output .check-output/uncapped_observability.json
	$(PYTHON) scripts/verify_binary_uncapped_observability.py --output .check-output/binary_uncapped_observability.json
	$(PYTHON) scripts/verify_fixed_clock_observability.py --output .check-output/fixed_clock_observability.json
	$(PYTHON) scripts/verify_prl_exploration.py --output .check-output/prl_exploration.json
	$(PYTHON) scripts/verify_kinetic_parity.py --output .check-output/kinetic_parity.json
