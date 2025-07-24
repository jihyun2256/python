#operator6.py
#논리 연산자 

score = 90 

result = 0 <= score <= 100
print(result)

score = 90 
result = score >= 0 and score <= 100
print(result)

result = score < 0 or score > 100
print(result)

flag = True

result = not flag
print(result)