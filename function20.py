#function20.py

def menu():
    print('1: 삼각형')
    print('2: 사각형')
    print('3: 원')
    selection = int(input('면적을 계산할 도형을 선택하세요: '))
    return selection

# def triangle(tb,th):
#     tri = 
#     return try

# def ftoc(f):
#     temp = (f-32.0)*5.0/9.0
#     return temp

# def input_tb():
#     tb = input(input("밑변: "))
#     return tb

# def input_th():
#     th = int(input("높이: "))
    return th

def square(s1, s2):
    squ = (s1 * s2)
    return squ

def input_s1():
    s1 = int(input("가로 : "))
    return s1

def input_s2():
    s2 = int(input("세로: "))
    return s2



def main():
    while True:
        index = menu()
        if index == 1:
            t = int(input("가로 : "))
            t1 = int(input("세로: "))
            result = square(t,t1)
            print("사각형의 면적 : ", result, "\n")
        # elif index == 2:
        #     t = input_f()
        #     t2 = ftoc(t)
        #     print(" = ", t2, "\n")
        else:
            break
main()