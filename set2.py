#set2.py

a = {1, 2, 3}
b = {2, 3, 4}

#합집합
print(a.union(b))
print(a | b)

#교집합
print(a.intersection(b))
print(a & b)

#차집합
print(a.difference(b))
print(a - b)

#대칭 차집합
print(a.symmetric_difference(b))
print(a ^ b)


