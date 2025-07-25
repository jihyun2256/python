#list2.py
#list에 대한 예제 프로그램입니다.

# _list = []

# print(_list)
# print(type(_list))
# print(len(_list))

list1 = [1, 2, 3, 4, 5]
print(list1)

#print(dir(list1))  #__iter__ : 반복 가능 객체 / dir():해당 객체의 속성과 메서드를 출력

#for 문을 사용하여 리스트 요소를 출력하시오.

for i in list1:
    print(i, end=' ')

list2 = list((1, 2, 3, 4, 5))

print()
print('='* 50)

print(list2)
print(type(list2))


list3 = [1, '홍길동', 100, 100, 100]

print()
print('='* 50)

for i in list3:
    print(i, end='\t')