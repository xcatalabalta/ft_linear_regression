# ft_linear_regression
An introduction to machine learning:  a linear function trained with a gradient descent algorithm.
It includes scripts to visualize the dataset and the regression adjustments.

## Requirements

- Python 3 (tested with `python3`)
- Dependencies listed in `requirements.txt` (installed via the steps below)

## Setup

The project uses a virtual environment so dependencies stay local to the
project and require no system-wide install (no `sudo` needed).

```bash
# 1. Create the virtual environment (once)
python3 -m venv my_venv

# 2. Activate it (every new terminal session)
source my_venv/bin/activate

# 3. Install the dependencies (once)
pip install --no-cache-dir -r requirements.txt

# Shortcut. All in a single line:
python3 -m venv my_venv;source my_venv/bin/activate;pip install --no-cache-dir -r requirements.txt
```

After the above, the prompt should now show `(my_venv)`, meaning the environment is active.
To leave it later, run `deactivate`.

## Running

With the environment active:

```bash
# Run the desired program
# Ideally:
python priceEstimation.py
python VisualizeData.py
python train.py
python priceEstimation.py
python VisualizeResult.py
python precision.py
```
Afterwards it is strongly recommended to deactivate the environment:
```bash
deactivate
# If you have already finished the evaluation, you can delete the output files:
# Manually:
rm -rf __pycache__ */__pycache__ *.pyc
rm -f *.json
rm -f normalized_data.csv
rm -rf my_venv
#  Or with make fclean
make fclean
```
## Use of the Makefile
The project has a Makefile to ease the installation and (probably) the evaluation.
### Evaluating using only the Makefile:
The Makefile contains the following rules that you can use for the evaluation:
  - all: Default target, it builds the environment.
  - setup: Build the environment.
  - data: Show the data visualization
  - predict: Run the price estimation as specified in the subject.
  - train: Train the model (produces thetas.json, thetas_norm.json, normalized_data.csv).
  - plot: Show the 2x2 visualization (requires train to have run first).
  - precision: Report model precision (only has sense if train has run first).
  - clean: Remove bytecode caches and generated data files.
  - fclean: Remove everything generated, including the virtual environment.
  - re: Rebuild from scratch.
### Evaluating using make and the terminal commands:
  ```bash
  # Setup with make:
  make
  # Activate the environment:
  source my_venv/bin/activate
  # Run the desired programs (as in the #Running section of this document)
  python priceEstimation.py
  python VisualizeData.py
  python train.py
  python priceEstimation.py
  python VisualizeResult.py
  python precision.py
  # Once finished, 
  deactivate
  make fclean
  ```

## Notes

- The `my_venv/` folder is intentionally not tracked in git. It is rebuilt from
  `requirements.txt` with the setup steps above.
- If anything in the environment breaks, delete and recreate it:

```bash
rm -rf my_venv
python3 -m venv my_venv
source my_venv/bin/activate
pip install --no-cache-dir -r requirements.txt
```
