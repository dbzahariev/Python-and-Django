import math

shells = {}
while True:
    data = input()
    if data == 'Aggregate':
        for region, shells_sizes in shells.items():
            giant = math.ceil(sum(shells_sizes) - (sum(shells_sizes) / len(shells_sizes)))
            shells_str = ", ".join(map(str, shells_sizes))
            print(f'{region} -> {shells_str} ({giant})')
        break
    else:
        region, shell = data.split(' ')
        shell = int(shell)
        if region not in shells:
            shells[region] = []
        if shell not in shells[region]:
            shells[region].append(shell)
