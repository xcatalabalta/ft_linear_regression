import matplotlib.pyplot as plt
import csv
import numpy as np
from priceEstimation import get_thetas

km = []
price = []

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        km.append(float(row[0]))
        price.append(float(row[1]))

thetas = get_thetas()
theta_0 = thetas.get("theta_0", 0)
theta_1 = thetas.get("theta_1", 0)
line = theta_1 * np.array(km) + theta_0
if theta_0 != 0 or theta_1 != 0:
    plt.plot(km, line, color='red', label='Regression Line')
plt.scatter(km, price, label='Data Points')
plt.xlabel("km")
plt.ylabel("Price")
plt.title("Car Price vs. km with Regression Line")
plt.legend()
plt.show()
