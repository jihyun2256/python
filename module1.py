#module1.py
#파이썬 모듈에 대한 예제 프로그램입니다. 


import random

colors = ['red', 'green', 'blue', 'white']


print(random.choice(colors))

#로또 번호 생성 : unique

lotto_nums = random.sample(range(1,46, 1), 6)

print(f'lotto_nums : {lotto_nums}')