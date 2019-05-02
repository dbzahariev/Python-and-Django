purchased_food = int(input()) * 1000

all_food_needed = 0
while True:
    eaten_food = input()
    if eaten_food == "Adopted":
        break
    eaten_food = int(eaten_food)
    all_food_needed += eaten_food
if purchased_food >= all_food_needed:
    print(f'Food is enough! Leftovers: {purchased_food - all_food_needed} grams.')
else:
    print(f'Food is not enough. You need {all_food_needed - purchased_food} grams more.')
