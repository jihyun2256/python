#if3.py
#조건문에 대한 예제 프로그램입니다

# x, y, max_value = 10, 5, 0
# if x > y:
#     max_value= x
# else:
#     max_value = y

# print(f'max_vlaue: {max_value}')

x, y = 10, 5
max_value = (x if x > y else y)
print(f'max_value: {max_value}')