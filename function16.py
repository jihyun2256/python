#function16.py
#변수의 범위에 대한 예제 프로그램입니다.

def sub():
    #지역 변수
    s = 'I like a banana'
    print(s)

#함수 호출
sub()

print(f'sub() s : {s}')