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
pip install -r requirements.txt
```

After the above, the prompt should now show `(my_venv)`, meaning the environment is active.
To leave it later, run `deactivate`.

## Running

With the environment active:

```bash
# Plot the dataset (price vs. kilometers)
python VisualizeData.py
```

## Notes

- The `my_venv/` folder is intentionally not tracked in git. It is rebuilt from
  `requirements.txt` with the setup steps above.
- If anything in the environment breaks, delete and recreate it:

  ```bash
  rm -rf my_venv
  python3 -m venv my_venv
  source my_venv/bin/activate
  pip install -r requirements.txt
  ```
