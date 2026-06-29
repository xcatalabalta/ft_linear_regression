import matplotlib.pyplot as plt
from priceEstimation import get_thetas
from VisualizeData import read_csv, draw_data
from VisualizeRegression import draw_regression


def main():
    km, price = read_csv("data.csv")
    try:
        km_norm, price_norm = read_csv("normalized_data.csv")
    except OSError:
        print("Error: normalized_data.csv file not available. "
              "Please run the training script first.")
        return
    km_norm, price_norm = read_csv("normalized_data.csv")

    t = get_thetas("thetas.json")
    t0, t1 = t.get("theta_0", 0), t.get("theta_1", 0)
    tn = get_thetas("thetas_norm.json")
    t0n, t1n = tn.get("theta_0", 0), tn.get("theta_1", 0)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    draw_data(axes[0][0], km, price, "Original data")
    draw_data(axes[0][1], km_norm, price_norm,
              "Normalized data", xlabel="km (normalized)")
    draw_regression(axes[1][0], km, price, t0, t1,
                    "Original data + regression")
    draw_regression(axes[1][1], km_norm, price_norm, t0n, t1n,
                    "Normalized data + regression", xlabel="km (normalized)")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
