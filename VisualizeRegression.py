import matplotlib.pyplot as plt
import numpy as np
from priceEstimation import get_thetas
from VisualizeData import read_csv, draw_data


def draw_regression(ax, km, price, theta_0, theta_1,
                    title="Car Price vs km with Regression Line", xlabel="km"):
    draw_data(ax, km, price, title, xlabel)
    km_arr = np.array(km)
    line = theta_0 + theta_1 * km_arr
    if theta_0 != 0 or theta_1 != 0:
        ax.plot(km_arr, line, color="red", label="Regression Line")
    ax.legend()


def main():
    km, price = read_csv("data.csv")
    thetas = get_thetas("thetas.json")
    t0, t1 = thetas.get("theta_0", 0), thetas.get("theta_1", 0)
    fig, ax = plt.subplots()
    draw_regression(ax, km, price, t0, t1)
    plt.show()


if __name__ == "__main__":
    main()
