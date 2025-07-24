# #if4.py
# # 정수를 입력 받아서 짝수인지 홀수인지 출력하는 프로그램

# num1 = int(input('정수를 입력하세요'))

# if num1 % 2 == 0:
#     print('짝수')

# else: 
#     print('홀수')

#if문에 대한 예제 

age, height = 11,170

if age >= 10 and height >= 165:
    print('놀이기구를 탈 수 있다')

else:
    print('놀이기구를 탈 수 없습니다')

if age< 10 or height <165:
    print('놀이기구를 탈 수 없습니다')
else:
    print('놀이기구를 탈 수 있다')