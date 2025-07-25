#list6.py

colors = ['red', 'green', 'blue', 'white', 'black']

#colors 리스트 정보를 조회하여 출력하시오
#인덱스, 요소 (항목)
#0, 'red'

for i in range(len(colors)):
    print(f'colors[{i}] : {colors[i]}')

# 'blue' -> 'yellow'

colors[0] = 'yellow'
print(colors[0])