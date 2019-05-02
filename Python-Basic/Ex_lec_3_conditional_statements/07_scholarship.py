import math

income = float(input())
grade = float(input())
minimal_wage = float(input())

social = 0
if income < minimal_wage and grade > 4.5:
    social = minimal_wage * 0.35
good_Grate = 0
if grade >= 5.5:
    good_Grate = grade * 25

if social + good_Grate == 0:
    print("You cannot get a scholarship!")
elif social > good_Grate:
    print(f"You get a Social scholarship {math.floor(social)} BGN")
elif good_Grate >= social:
    print(f"You get a scholarship for excellent results {math.floor(good_Grate)} BGN")
