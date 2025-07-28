#exception2.py
#exception handling에 대한 예제 프로그램입니다.


#함수 정의
def divide(a,b):

    if b == 0:
        raise ZeroDivisionError('0으로 나눌 수 없습니다.') #개발자가 강제로 예외 발생

    return a / b


#함수 호출
try:
    result = divide(10,0)
    print(f'result : {result}')
except ZeroDivisionError as err:
    print(f'err : {err}')

print('end')
