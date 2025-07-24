#function5.py
#사용자 정의 함수에 대한 예제 프로그램입니다.

#원의 면적을 구하는 함수 정의 
def get_area(radius):
    return 3.14 * radius ** 2


#함수 호출 
result = get_area(3)
print(type(result))

print(f'반지름이 3인 원의 면적 ={result}')


result = get_area(20)
print(f'반지름이 20인 원의 면적 ={result}')