#string6.py
#string 함수에 대한 예제 프로그램

str = 'python string'

idx = str.find('string')

print(f'index:{idx}')
print(f'str 문자열의 길이:{len(str)}')
print(f't 문자의 개수:{str.count("t")}')
print(f'str 대문자로 변환:{str.upper()}')
print(f'str : str')

str1 = '      python string'

str2 = str1.strip()
print(f'str2 : {str2}')
print(f'str2 문자열의 길이 : {len(str2)}')
print(f'str1 문자열의 길이 : {len(str1)}')





str3 = 'python string'
str4 = str3. replace('string', '문자열')
print(f'str4: {str4}')