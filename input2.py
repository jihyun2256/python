#input2.py
#두 정수를 키보드로 입력 받아서 사칙 연산을 출력하세요 
a,b = input('두 개의 정수를 입력하세요. (공백을 포함하세요.)').split()
#공백이 split의 기준이기 때문에 공백이 있어야함

print(f'a : {a}, b : {b}')
print(type(a))
print(type(b))

a, b = list(map(int, input('두 개의 정수를 입력하세요(공백)').split()))

print(f'a ; {a}, b : {b}')
print(type(a))
print(type(b))

c, d = list(map(int, input('두 개의 정수를 입력하세요').split(sep=",")))


print(f'c ; {c}, d : {d}')
print(type(c))
print(type(d))