#lamda.py
#람다 함수에 대한 예제 프로그램 

#함수 정의 
# def hello(user_name):
#    return "Hello, " + user_name

hello = lamda(user_name: 'Hello, ' + user_name)

print(type(hello)) #fuction 객체

print(hello('kso'))