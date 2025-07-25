#dic10.py

dic = {'a':1, 'b':2, 'c':3}

for key in dic.keys():
    print(key, dic[key])


for key in dic:
    print(key, dic.get(key))

for value in dic.values():
    print(value)


for key, value in dic.items(): #언패킹
    print(key, value)

value = dic.pop('b')
print(f'value : {value}')
print(dic)

dic.clear()
print(dic)