#list14.py

menu = [['칼국수', 6000], ['비빔밥', 5500], ['돼지국밥', 7000], 
              ['돈까스', 7000], ['김밥', 2000], ['라면', 2500]]

# 3. 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가 할 때 기존에 동일한 메뉴가 존재하는 경우 가격만 변경 되도록 코드를 작성 하시오.
new_name, new_price = input('메뉴와 가격을 입력하세요. : ').split()


is_updated = False
for i in range(len(menu)):
    if menu[i][0] == new_name:
        menu[i][1] = new_price
        is_updated = True
        print(f'{new_name} 메뉴 가격이 {new_price}로 변경되었습니다.')
        break

if not is_updated:
    menu.append([new_name, new_price])

print(menu)

