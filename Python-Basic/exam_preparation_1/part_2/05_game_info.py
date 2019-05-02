team_name = input()
count_matches = int(input())

all_minutes = 0
continue_matches = 0
penalties_matches = 0
for i in range(0, count_matches):
    minutes = int(input())
    all_minutes += minutes
    if minutes > 90 and minutes<=120:
        continue_matches += 1
    if minutes > 120:
        penalties_matches += 1

print(f'{team_name} has played {all_minutes} minutes. Average minutes per game: {(all_minutes / count_matches):.2f}')
print(f'Games with penalties: {penalties_matches}')
print(f'Games with additional time: {continue_matches}')
