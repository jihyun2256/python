#while3.py
#학생들의 성적을 입력받아 합계와 평균을 구하시오 
#성적 입력을 끝내고 싶을 때는 점수에 음수를 입력한다. 
#평균은소수 둘째자리까지 나타낸다.

# 학생들의 성적합계와 평균을 계산합니다.
# 입력을 종료하려면 음수를 입력하세요
# 성적을 입력하세요: 88
# 성적을 입력하세요: 98
# 성적을 입력하세요: 76
# 성적을 입력하세요: -1
# 합계:   262       
# 평균: 87.33

total = 0
count = 0 
is_continue = True


while is_continue:
    score = int(input('성적을 입력하세요 :'))
    if score >= 0:
        total += score
        count += 1
    else: 
        is_continue = False
avg = total / count 
    
print(f'합계 : {total}')
print(f'평균 : {avg:.2f}')