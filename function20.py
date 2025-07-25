# function20.py


def menu():
    print('1. 삼각형')
    print('2. 사각형')
    print('3. 원')
    print('4. 종료')
    selection = int(input('면적을 계산할 도형을 선택하세요 : '))
    return selection


def get_triangle_area(base, height):
    '''삼각형의 넗이를 구하다.'''
    return 0.5 * base * height

def get_rectangle_area(width, height):
    '''사각형의 넗이를 구하다.'''    
    return width * height

def get_circle_area(radius):
    '''원의 넗이를 구하다.'''    
    return 3.14 * radius ** 2

def input_triangle():
    base = int(input('밑변 : '))
    height = int(input('높이 : '))    
    return [base, height]

def input_rectanble():
    width = int(input('가로의 길이 : '))
    height = int(input('세로의 길이 : '))
    return [width, height]

def input_circle():
    radius = int(input('반지름 : '))
    return radius

def main():
    while True:
        selection = menu()

        if selection == 1:
            base, height = input_triangle()
            result = get_triangle_area(base, height)
            print(f'삼각형의 면젹 : {result}')

        elif selection == 2:
            width, height = input_rectanble()
            result = get_rectangle_area(width, height)
            print(f'사각형의 면젹 : {result}')

        elif selection == 3:
            radius = input_circle()
            result = get_circle_area(radius)
            print(f'원의 면젹 : {result}')
        else:
            break 



main()