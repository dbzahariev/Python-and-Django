inventory = input().split()

while True:
    data = input()
    if data == 'Fight!':
        break
    data = data.split()
    command = data[0]
    equipment = data[1]

    if command == 'Buy' and equipment not in inventory:
        inventory.append(equipment)
    elif command == 'Trash' and equipment in inventory:
        inventory.remove(equipment)
    elif command == 'Repair' and equipment in inventory:
        inventory.remove(equipment)
        inventory.append(equipment)
    elif command == 'Upgrade':
        equipment = equipment.split('-')
        if equipment[0] in inventory:
            inventory.insert(inventory.index(equipment[0]) + 1, f'{equipment[0]}:{equipment[1]}')

print(' '.join(inventory))
