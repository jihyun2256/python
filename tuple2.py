#tuple2.py
#패킹과 언패킹 

#paking
_tuple = 1,2

print(_tuple)
print(type(_tuple))

#unpacking
a, b, c = (1,2,3)

print(f'a = {a}, b = {b}, c = {c}')


p = (1,2), (3,4)

print(p)

x, y = p

print(x)
print(y)