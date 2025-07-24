#function8.py

#위치 인수 (positional augument), 키워드(keyword) 인수

def calc(x, y, z,):
    print(f'x = {x}, y = {y}, z = {z}')

#호출 
calc(1, 2, 3) #positional augument

calc(y=1, x=2, z=3) #keyword augument

calc(1, z=3, y=2)