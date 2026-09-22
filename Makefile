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
