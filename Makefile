# ft_linear_regression — Makefile
# Self-contained: targets call the venv's interpreter directly,
# so no manual activation is ever required.

VENV   := my_venv
PY     := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip
FLAKE8 := $(VENV)/bin/flake8

# Default target: build the environment.
all: setup

# Build the venv and install dependencies (idempotent via the sentinel).
setup: $(VENV)/.installed

$(VENV)/.installed: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --no-cache-dir --upgrade pip
	$(PIP) install --no-cache-dir -r requirements.txt
	touch $(VENV)/.installed

# Train the model (produces thetas.json, thetas_norm.json, normalized_data.csv).
train: setup
	$(PY) train.py

# Predict a price (prompts for a mileage).
predict: setup
	$(PY) priceEstimation.py

# Show the 2x2 visualization (requires train to have run first).
plot: setup
	$(PY) VisualizeResult.py

# Show the data visualization
data: setup
	$(PY) VisualizeData.py

# Report model precision (requires train to have run first).
precision: setup
	$(PY) precision.py

# Lint the project's Python files (my_venv excluded via .flake8).
lint: setup
	$(FLAKE8) .

# Remove bytecode caches and generated data files.
clean:
	rm -rf __pycache__ */__pycache__ *.pyc
	rm -f *.json
	rm -f normalized_data.csv

# Remove everything generated, including the virtual environment.
fclean: clean
	rm -rf $(VENV)

# Rebuild from scratch.
re: fclean all

.PHONY: all setup data train predict plot precision lint clean fclean re