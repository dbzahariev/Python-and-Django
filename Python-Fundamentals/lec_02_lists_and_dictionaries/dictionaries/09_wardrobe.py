lines = int(input())
wardrobe = {}

for line in range(0, lines):
    clothes = input()
    color, types = clothes.split(' -> ')
    if color not in wardrobe.keys():
        wardrobe[color] = {}
    for this_type in str(types).split(','):
        if this_type in wardrobe[color]:
            wardrobe[color][this_type] += 1
        else:
            wardrobe[color][this_type] = 1

display_color, display_item, *rest = input().split(' ')

for color, items in wardrobe.items():
    print(f'{color} clothes:')
    for item, quantity in items.items():
        print(
            f'* {item} - {quantity}' + ' (found!)' if display_color == color and display_item == item else f'* {item} - {quantity}')
