#money.py
#투자금이 2배가 되는데 걸리는 시간(연도) 계산

target = 2000
money = 1000
year = 0
rate = 0.07

while money < target:
    money = money+ money * rate
    year = year + 1
    print(f'money : {int(money)}원, year : {year}')

print(f'{year}년')
