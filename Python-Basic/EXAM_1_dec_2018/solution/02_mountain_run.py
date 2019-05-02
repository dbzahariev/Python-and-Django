import math

record = float(input())
raztoqnie = float(input())
vreme = float(input())

aa = (raztoqnie * vreme)
bb = (math.floor(raztoqnie / 50) * 30)  # na vseki 50 metra
obshto_vreme = (aa + bb)

diff = record - obshto_vreme

if diff <= 0:
    print(f'No! He was {abs(diff):.2f} seconds slower.')
else:
    print(f'Yes! The new record is {obshto_vreme:.2f} seconds.')
