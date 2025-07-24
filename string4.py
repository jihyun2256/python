#sting4.py
#문자열의 길이 구하기 

str = 'hello'
length = len(str)

print(f'str 문자열의 길이 : {len(str)}')


str1 = ' hello '
length = len(str1)
print(f'str 문자열의 길이 : {len(str1)}')

print(f'str 문자열의 길이 : {len(str1.strip())}') # strip(): 공백 제거 