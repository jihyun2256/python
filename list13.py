#list13.py

menu = [['칼국수', 6000], ['비빔밥', 5500], ['돼지국밥', 7000], 
              ['돈까스', 7000], ['김밥', 2000], ['라면', 2500]]

# 위의 리스트 구조를 보고 아래에서 요구하는 결과가 반영 되도록 코드를 작성 하시오.

# 1. 비빔밥과, 돈까스의 가격을 출력 하시오.
#print(f'칼국수 가격 : {menu[0][1]}, 비빔밥 가격 : {menu[1][1]}')

# for name, price in menu: #언패킹
for i in menu:
    if menu[i][1] == '비빔밥' or menu[i][1] == '칼국수':
        print(f'{name} : {price}')
    

# 2. 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가하는 코드를 작성 하시오.
name,price = input('메뉴와 가격을 입력하세요. : ').split()
menu.append([menu], int(price))


