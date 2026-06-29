import sys
import json
import math


def get_thetas(file_path):
    """
    Reads the thetas from a JSON file and returns them as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            thetas = json.load(file)
        return thetas
    except (FileNotFoundError, json.JSONDecodeError):
        return {"theta_0": 0, "theta_1": 0}


def estimate_price(theta_0, theta_1, mileage):
    """
    Estimates the price of a car based on kilometers and thetas.
    """
    return theta_0 + (theta_1 * mileage)


def main():
    file_path = "thetas.json"
    thetas = get_thetas(file_path)
    theta_0 = thetas.get("theta_0", 0)
    theta_1 = thetas.get("theta_1", 0)
    neg_km = "km cannot be negative. Run the program again with a valid input."

    try:
        km = float(input("Enter the number of kilometers: "))
        if km < 0:
            print(neg_km)
            sys.exit(1)
        elif math.isnan(km) or math.isinf(km):
            print("Come on! Run the program again with a valid input.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a numeric value for kilometers.")
        sys.exit(1)

    price = estimate_price(theta_0, theta_1, km)

    if price <= 0 and (theta_0 != 0 or theta_1 != 0):
        print(f"Estimated price for {km} kilometers: "
              f"\033[91m{price:.2f}\033[00m")
    else:
        print(f"Estimated price for {km} kilometers: {price:.2f}")


if __name__ == "__main__":
    main()
