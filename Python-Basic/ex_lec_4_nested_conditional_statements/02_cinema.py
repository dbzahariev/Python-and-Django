type_projection = input().lower()
count_row = int(input())
count_columns = int(input())

total_seats = count_row * count_columns
if type_projection == "premiere":
    print(f"{(total_seats*12):.2f} leva")
elif type_projection == "normal":
    print(f"{(total_seats*7.5):.2f} leva")
elif type_projection == "discount":
    print(f"{(total_seats*5):.2f} leva")
