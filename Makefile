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
