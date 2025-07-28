#any.py
#any, all 함수에 대한 예제 

result = any([True, False, False, False, False])
print(f'result: {result}')

result = any([False, False, False, False])
print(f'result: {result}')

result = all([True, False, False, False, False])
print(f'result: {result}')

result = all([True, True, True, True])
print(f'result: {result}')