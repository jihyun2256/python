#while2.py
#사용자가 입력한 숫자를 더해서 합을 계산하는 프로그램
#입력을 계속할 건지 물어서 yes를 입력하면 다음 숫자 입력
#no를 입력하면 합을 출력

total = 0 #합계를 저장할 변수 
answer = 'yes'

while answer == 'yes':
    num = int(input('숫자를 입력하세요'))
    total += num
    answer = input('계속 (yes/no) ?')

print(f'입력한 숫자들의 합 : {total}')
