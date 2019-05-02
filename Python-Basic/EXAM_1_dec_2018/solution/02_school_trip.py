import math

count_days = int(input())
count_food = int(input())
count_food_for_days_first_dog = float(input())
count_food_for_days_second_dog = float(input())
count_food_for_days_third_dog = float(input())

first_dog = count_days * count_food_for_days_first_dog
second_dog = count_days * count_food_for_days_second_dog
third_dog = count_days * count_food_for_days_third_dog

all_food = first_dog + second_dog + third_dog
if all_food > count_food:
    print(f'{math.ceil(all_food - count_food)} more kilos of food are needed.')
else:
    print(f'{math.floor(abs(all_food - count_food))} kilos of food left.')
