#list18.py
#list comprehension

fruits = ['apple', 'peach', 'banana', 'orange', 'pineapple']

result = [fruit for fruit in fruits if fruit[0] == 'p']

print(result)


# 리스트에 들어있는 과일 중에서 문자열의 길이가 6자 이상인 과일만 출력

result = [fruit for fruit in fruits if len(fruit) >= 6]

print(result)