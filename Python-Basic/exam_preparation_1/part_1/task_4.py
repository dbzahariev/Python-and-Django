best_player_name = ''
best_player_goal = -1
while True:
    text = input()
    if text == 'END':
        break
    player_name = text
    player_goals = int(input())
    if player_goals > best_player_goal:
        best_player_name = player_name
        best_player_goal = player_goals
    if player_goals >= 10:
        break
print(f"{best_player_name} is the best player!")
if best_player_goal >= 3:
    print(f'He has scored {best_player_goal} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_player_goal} goals.')
