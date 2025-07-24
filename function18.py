##function18.py

#함수 안에서 전역 변수 사용하기 

def calculate_area(radius):
    global area
    area = 3.14 * radius ** 2
    return

r = float(input('원의 반지름 : '))

calculate_area(r)

print(area)