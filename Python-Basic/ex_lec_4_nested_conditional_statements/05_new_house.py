flowers = input()
count = float(input())
budget = float(input())

type_flowers = {"Roses": 5, "Dahlias": 3.80, "Tulips": 2.80, "Narcissus": 3, "Gladiolus": 2.50}
all_prices = type_flowers[flowers] * count
if all_prices > budget:
    print(f"Not enough money, you need {all_prices-budget:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {count:.0f} {flowers} and {budget - all_prices:.2f} leva left.")
