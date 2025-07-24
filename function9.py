#function9.py

#가변 인수 함수에 대한 프로그램입니다. 

#두 수의 합을 구하는 함수 
#세 숫자의 합을 구하는 함수
#네 숫자의 합을 구하는 함수 

#함수 정의 
def sum(*args):  #(1,2)
    # print(f'args : {args}')
    # print(f'args type: {type(args)}')
    total = 0
    for i in args: #sequence : list, tuple, string 
        total += i
    return total

#함수 호출
print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4))