count_groups = int(input())

all_people = 0
count_musala = 0
count_montblanc = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0
for i in range(0, count_groups):
    count_people = int(input())
    all_people += count_people
    if count_people <= 5:
        count_musala += count_people
    elif 6 <= count_people <= 12:
        count_montblanc += count_people
    elif 13 <= count_people <= 25:
        count_kilimanjaro += count_people
    elif 26 <= count_people <= 40:
        count_k2 += count_people
    elif count_people >= 41:
        count_everest += count_people
print(f'{count_musala / all_people * 100:.2f}%')
print(f'{count_montblanc / all_people * 100:.2f}%')
print(f'{count_kilimanjaro / all_people * 100:.2f}%')
print(f'{count_k2 / all_people * 100:.2f}%')
print(f'{count_everest / all_people * 100:.2f}%')
