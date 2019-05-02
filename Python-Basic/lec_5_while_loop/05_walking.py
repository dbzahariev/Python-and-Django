new_steps = input()
all_steps = 0
while True:
    if not new_steps == "Going home":
        all_steps += int(new_steps)
    if all_steps >= 10000:
        print(f"Goal reached! Good job!")
        break
    if new_steps == "Going home":
        all_steps += int(input())
        if all_steps >= 10000:
            print(f"Goal reached! Good job!")
        else:
            print(f"{10000 - all_steps} more steps to reach goal.")
        break
    else:
        new_steps = input()
