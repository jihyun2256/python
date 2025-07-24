#continue2.py
#사용자로부터 ‘-’이 포함된 계좌 번호를 입력받아 ‘-’을 삭제한 문자열 출력

account_num = input('계좌번호를 입력하세요 : ')

temp = ''
for ch in account_num:
    if ch =='-':
        continue
    temp += ch   
print(temp)
        