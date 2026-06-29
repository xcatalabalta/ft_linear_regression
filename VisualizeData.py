import matplotlib.pyplot as plt
import csv


def read_csv(file_path):
    """
    Reads km and price data from a CSV
    Returns them as two lists.
    """
    km, price = [], []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            km.append(float(row[0]))
            price.append(float(row[1]))
    return km, price


def draw_data(ax, km, price,
              title="Car Price vs. Kilometers", xlabel="Kilometers"):
    """
    Draws the data points on the given axes.
    """
    ax.scatter(km, price, label="Data Points")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Price")
    ax.set_title(title)


def main():
    km, price = read_csv("data.csv")
    fig, ax = plt.subplots()
    draw_data(ax, km, price)
    plt.show()


if __name__ == "__main__":
    main()
