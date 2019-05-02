number = float(input())
mu_in = input()
mu_out = input()
mu = {"m": 1, "mm": 1000, "cm": 100, "mi": 0.000621371192, "in": 39.3700787, "km": 0.001, "ft": 3.2808399,
      "yd": 1.0936133}
meters = number / mu[mu_in]
output = meters * mu[mu_out]
print(output)
