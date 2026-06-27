import matplotlib.pyplot as plt
import csv

km = []
price = []

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        km.append(float(row[0]))
        price.append(float(row[1]))

plt.scatter(km, price)
plt.xlabel("Kilometers")
plt.ylabel("Price")
plt.title("Car Price vs. Kilometers")
plt.show()