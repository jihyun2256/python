#for7.py
#구구단 가로 출력


for dan in range(2,10,1):
    print(f'=={dan}단==', end = '\t')
print()

for x in range(1,10,1):
    for y in range(2,10,1):
        print(f'{y} x {x} = {x * y}', end='\t')
    print()