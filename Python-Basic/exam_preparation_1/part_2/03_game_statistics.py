minutes = float(input())
name = input()

if minutes == 0:
    print('Match has just began!')
elif minutes < 45:  # TODO: tuk moje da e <=
    print('First half time.')
else:
    print('Second half time.')

if 1 <= minutes <= 10:
    print(f'{name} missed a penalty.')
    if minutes % 2 == 0:
        print(f'{name} was injured after the penalty.')
elif 10 < minutes <= 35:
    print(f'{name} received yellow card.')
    if minutes % 2 == 1:
        print(f'{name} got another yellow card.')
elif 35 < minutes < 45:
    print(f'{name} SCORED A GOAL !!!')
elif 45 < minutes <= 55:
    print(f'{name} got a freekick.')
    if minutes % 2 == 0:
        print(f'{name} missed the freekick.')
elif 55 < minutes <= 80:
    print(f'{name} missed a shot from corner.')
    if minutes % 2 == 1:
        print(f'{name} has been changed with another player.')
elif minutes > 80:
    print(f'{name} SCORED A GOAL FROM PENALTY !!!')
