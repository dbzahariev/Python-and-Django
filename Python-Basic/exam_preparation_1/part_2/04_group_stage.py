name_team = input()
count_matches = int(input())

all_points = 0
all_diff = 0
for i in range(0, count_matches):
    gol_in = int(input())
    gol_out = int(input())
    if gol_in > gol_out:
        all_points += 3
    if gol_in == gol_out:
        all_points += 1
    if gol_in < gol_out:
        all_points += 0
    diff = gol_in - gol_out
    all_diff += diff

if all_diff >= 0:
    print(f'{name_team} has finished the group phase with {all_points} points.')
    print(f'Goal difference: {all_diff}.')
else:
    print(f'{name_team} has been eliminated from the group phase.')
    print(f'Goal difference: {all_diff}.')
