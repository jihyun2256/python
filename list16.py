#list16.py
#리스트 컴프리헨션
#[표현식 for 변수 in iterable if  조건식]

_list = []
for i in range(1, 11, 1):
    _list.append(i ** 2)

print(_list)

_list = [i ** 2 for i in range(1, 11, 1)]

print(_list)