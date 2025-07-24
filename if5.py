#if5.py

#정수를 입력 받아서 양수, 음수, 0 인지를 출력하는 예제 프로그램

num1 = int(input('정수를 입력하세요 '))

# if num1 > 0 :
#     print('양수') 
# elif num1 < 0:
#     print('음수')
# else:
#     print('0')

if num1 == 0 :
    print('0') 
elif num1 > 0:
    print('양수')
else:
    print('음수')