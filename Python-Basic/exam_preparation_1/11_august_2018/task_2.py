km = int(input())
razhod = int(input())
price = float(input())
budget = int(input())

litter_money = km * razhod / 100
all_money = litter_money * price
diff = budget - all_money
if diff >= 0:
    print(f'You can go home. {diff:.2f} money left.')
else:
    print(f"Sorry, you cannot go home. Each will receive {(budget / 5):.2f} money.")
