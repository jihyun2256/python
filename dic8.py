#dic8.py

k = ['a', 'b', 'c', 'd']

dic1, dic2 = {}, {}

dic1 = dic1.fromkeys(k)
dic2 = dic2.fromkeys(k,1)

print(dic1)
print(dic2)