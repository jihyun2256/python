#if2.py
#if else 구문 (양자택일) 에 대한 예제
# 성적이 0~100 사이의 정수가 아닌 경우는 '성적을 정확히 입력하세요'
#성적이 0~100 사이의 정수인 경우 60점이상인 경우 합격, 그렇지 않은 경우 불합격을 출력하시오

score = int(input('성적을 입력하세요 '))

if score < 0 or score > 100:
    print('성적을 정확히 입력하세요.')
    exit(0)

if score >= 60:    
    print('합격입니다.')

else: #score < 60
    print('불합격입니다.')

# price = int(input('상품의 가격'))

# if price > 20000: 11
#     shipping_cost = 0
# else:
#     shipping_cost = 3000

# #배송비를 출력한다
# print("배송비 =", shipping_cost)

