# ft_linear_regression — Makefile
# Self-contained setup: `make run` builds the environment (if needed)
# and runs the program. No manual venv activation required.

VENV := my_venv
PIP  := $(VENV)/bin/pip

# Default target: build the environment.
all: setup

# Create the venv and install dependencies.
# The sentinel file ($(VENV)/.installed) makes this idempotent:
# the env is only rebuilt when requirements.txt changes.
setup: $(VENV)/.installed

$(VENV)/.installed: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --no-cache-dir --upgrade pip
	$(PIP) install --no-cache-dir -r requirements.txt
	touch $(VENV)/.installed

# Remove Python bytecode caches.
clean:
	rm -rf __pycache__ */__pycache__ *.pyc
	rm -f *.json
	rm -f normalized_data.csv

# Remove everything generated, including the virtual environment.
fclean: clean
	rm -rf $(VENV)

# Rebuild from scratch.
re: fclean all

.PHONY: all setup run clean fclean re