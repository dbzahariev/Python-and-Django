ml = float(input())
taped = 0
buttons = {"Easy": 50, "Medium": 100, "Hard": 200}
while ml > 0:
    ml -= buttons[input()]
    taped += 1
if ml == 0:
    print(f"The dispenser has been tapped {taped} times.")
else:
    print(f"{abs(ml):.0f}ml has been spilled.")

# Without dict

# ml = float(input())
# taped = 0
# while ml > 0:
#     buttons_input = input()
#     if buttons_input == "Easy":
#         ml -= 50
#     elif buttons_input == "Medium":
#         ml -= 100
#     elif buttons_input == "Hard":
#         ml -= 200
#     taped += 1
# if ml == 0:
#     print(f"The dispenser has been tapped {taped} times.")
# else:
#     print(f"{abs(ml):.0f}ml has been spilled.")
