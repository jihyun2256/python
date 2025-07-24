#exam2_4.py
#문자열중앙에 있는 문자를 출력한다.
#짝수개의 문자를 가진 문자열은 가운데 2개의 문자, 홀수개의 문자를 가진 문자열은 가운데 한 문자 출력


str = input('문자열을 입력하세요')
str_length = len(str)

if len(str) == 0:
     print('문자열을 정확히 입력하세요')
     exit(0)

if str_length % 2 == 0:
     mid = len(str) // 2
     print(str[mid - 1 : mid + 1]) #짝수개의 문자를 가진 문자열
else:
     mid = len(str) // 2
     print(str[mid]) #홀수개의 문자를 가진 문자열
