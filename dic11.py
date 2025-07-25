#dic11.py

#1. 다음의 메뉴와 가격을 Key와 Value로 사용하여 사전형 자료를 만드시오. (변수명은 menu)

menu = {'칼국수': 6000,
        '비빔밥': 5500,
        '돼지국밥': 7000,
        '돈까스': 7000,
        '김밥': 2000,
        '라면': 2500
}

menu['냉면'] = 1000
print(menu)

#2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에 해당하는 메뉴와 가격을 출력하는 코드를 작성하시오.

for name, price in menu.items():
    if price < 6000:
        print(f'{name} : {price}')

#3. 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가 할 수 있도록 하시오. (동일한 메뉴는 가격만 변경)

new_name, new_price  = input('메뉴와 가격을 입력하세요(냉면 10000) ').split()

# is_updated = False
# for name in menu.keys():
#     if name == new_name:
#         menu[name] = new_price

# if not is_updated:
#     menu[new_name] = new_price

menu.update({new_name: new_price})


print(menu)