#list17.py
#list comprehension

num_list = [2, 5, 8, 12, 3, 7]

result = [num for num in num_list if num % 2 == 0]

print(f'result : {result}')