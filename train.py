import sys
import json
import numpy as np


def get_points_from_csv(file_path):
    """
    Reads km and price points from a CSV file
    Returns them as two numpy arrays.
    """
    try:
        points = np.genfromtxt(file_path, delimiter=",", skip_header=1)
    except (OSError, ValueError):
        print(f'Warning: Failed to load file {file_path}')
        print('Check if the file exists and is in the correct format.')
        sys.exit(1)
    if points.ndim != 2 or points.shape[1] != 2 or np.isnan(points).any():
        print(f'Warning: Invalid data in {file_path}. Check file.')
        sys.exit(1)
    # print(f"Loaded {len(points)} points from {file_path}.")
    return points[:, 0], points[:, 1]  # km, price


def set_thetas(theta_0, theta_1, file_path):
    """
    Saves the thetas to a JSON file.
    """
    thetas = {"theta_0": theta_0, "theta_1": theta_1}
    try:
        with open(file_path, 'w') as file:
            json.dump(thetas, file, indent=2)
    except OSError:
        print("Error: Could not write to thetas.json file.")
        sys.exit(1)


def gradient_descent(km, price, theta_0, theta_1, learning_rate, iterations):
    """
    Performs gradient descent to optimize thetas.
    Print statements are commented out to reduce verbosity.
    """
    if iterations < 1:
        print("Error: iterations must be at least 1.")
        sys.exit(1)
    precision = 1e-7
    m = len(km)
    for i in range(iterations):
        predictions = theta_0 + (theta_1 * km)
        error = predictions - price
        step_0 = (learning_rate / m) * np.sum(error)
        step_1 = (learning_rate / m) * np.dot(error, km)
        theta_0 -= step_0
        theta_1 -= step_1
        if abs(step_0) < precision and abs(step_1) < precision:
            # print(f"Converged after {i + 1} iterations.")
            break
    # print(f"Final iterations: {i + 1}\n{step_0=}, {step_1=}")
    thetas = {"theta_0": theta_0, "theta_1": theta_1}
    return thetas


def save_normalized_data(km_norm, price_norm):
    """
    Saves the normalized data to a csv file.
    """
    try:
        np.savetxt("normalized_data.csv",
                   np.column_stack((km_norm, price_norm)),
                   delimiter=",", header="km_norm,price_norm", comments="")
    except OSError:
        print("Error: Could not write to normalized_data.csv file.")
        sys.exit(1)


def normalize_data(km, price, km_mean, km_std, price_mean, price_std):
    """
    Normalizes the km and price data.
    """
    km_norm = (km - km_mean) / km_std
    price_norm = (price - price_mean) / price_std
    save_normalized_data(km_norm, price_norm)

    return km_norm, price_norm


def denorm_thetas(th_0, th_1, km_mean, km_std, price_mean, price_std):
    """
    Denormalizes thetas based on the mean and std deviation of km and price.
    """
    th_1_denorm = th_1 * (price_std / km_std)
    th_0_denorm = price_mean + (th_0 * price_std) - (th_1_denorm * km_mean)

    return th_0_denorm, th_1_denorm


def print_sorted_points(points):
    """
    Prints the km and price points sorted ascending by km.
    Kept for debugging and learning purposes.
    """
    km = points[0]
    price = points[1]
    order = np.argsort(km)
    print("\nSorted points:")
    for i in order:
        print(km[i], price[i])


def print_norm_vs_denorm(km_norm, price_norm, km, price):
    """
    Prints the normalized and denormalized km and price points.
    Kept for debugging purposes.
    """
    print("\nNormalized vs Denormalized points:")
    for i in range(len(km)):
        print(f"Normalized: ({km_norm[i]:.4f}, {price_norm[i]:.4f})"
              f" | Denormalized: ({km[i]}, {price[i]})")


def main():
    # thetas = np.random.randn(2, 1)  # random initialization of thetas
    thetas = np.zeros((2, 1))  # zero initialization of thetas
    rate = 0.01
    itera = 1000
    lista = get_points_from_csv("data.csv")
    km_mean = np.mean(lista[0])
    km_std = np.std(lista[0])
    price_mean = np.mean(lista[1])
    price_std = np.std(lista[1])
    km_norm, price_norm = normalize_data(lista[0], lista[1],
                                         km_mean, km_std,
                                         price_mean, price_std)
    # print_norm_vs_denorm(km_norm, price_norm, lista[0], lista[1])
    thetas = gradient_descent(km_norm, price_norm,
                              thetas[0][0], thetas[1][0], rate, itera)
    set_thetas(thetas["theta_0"], thetas["theta_1"], 'thetas_norm.json')
    th_0_denorm, th_1_denorm = denorm_thetas(
        thetas["theta_0"], thetas["theta_1"],
        km_mean, km_std, price_mean, price_std)
    set_thetas(th_0_denorm, th_1_denorm, 'thetas.json')


if __name__ == "__main__":
    main()
