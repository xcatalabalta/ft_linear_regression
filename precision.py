import numpy as np
from priceEstimation import get_thetas
from train import get_points_from_csv


def rsme(theta_0, theta_1, km, price):
    """
    Computes the Root Mean Square Error (RMSE)
    Uses thetas and data points.
    """
    m = len(km)
    if m == 0:
        return float('inf')  # Avoid division by zero
    error_sum = np.sum((theta_0 + theta_1 * km - price) ** 2)
    rmse = (error_sum / m) ** 0.5
    return rmse


def r2_score(theta_0, theta_1, km, price):
    """
    Computes the R-squared (coefficient of determination)
    Uses thetas and data points.
    """
    m = len(km)
    if m == 0:
        return float('-inf')  # Avoid division by zero
    mean_price = np.mean(price)
    ss_total = np.sum((price - mean_price) ** 2)
    ss_residual = np.sum((price - (theta_0 + theta_1 * km)) ** 2)
    r2 = 1 - (ss_residual / ss_total) if ss_total != 0 else float('-inf')
    return r2


def main():
    thetas = get_thetas("thetas.json")
    t0, t1 = thetas.get("theta_0", 0), thetas.get("theta_1", 0)
    lista = get_points_from_csv("data.csv")
    km = lista[0]
    price = lista[1]
    rmse = rsme(t0, t1, km, price)
    r2 = r2_score(t0, t1, km, price)
    print(f"Max price: {max(price):.2f}\nMin price: {min(price):.2f}\n"
          f"Mean price: {np.mean(price):.2f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R-squared: {r2:.4f}")


if __name__ == "__main__":
    main()
