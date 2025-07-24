#while1.py
#구구단 9단을 반복문(while문)을 이용하여 출력

dan = int(input('원하는 단은 : '))

i = 1 #start : 시작값

while i <= 9: #stop
    print(f'{dan} * {i} = {dan * i}')
    i += 1 #step