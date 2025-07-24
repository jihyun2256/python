#function20.py

def menu():
    print('1: 삼각형')
    print('2: 사각형')
    print('3: 원')
    selection = int(input('면적을 계산할 도형을 선택하세요: '))
    return selection



def square_area(s1, s2):
    s_area = (s1 * s2)
    return s_area

def input_square():
    s1 = int(input("가로 : "))
    s2 = int(input("세로: "))
    return [s1,s2]




def main():
    while True:
        index = menu()
        if index == 1:
            t = int(input("밑변 : "))
            t1 = int(input("높이 : "))
            result = square(t,t1)
            print("삼각형의 면적 : ", result, "\n")
        elif index == 2:
            t = int(input("가로 : "))
            t1 = int(input("세로: "))
            result = square(t,t1)
            print("사각형의 면적 : ", result, "\n")
        elif index == 2:
            t = int(input("가로 : "))
            t1 = int(input("세로: "))
            result = square(t,t1)
            print("원의 면적 : ", result, "\n")
        else:
            break
main()