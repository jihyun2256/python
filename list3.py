#list3.py
#list에 대한 예제 프로그램
#인덱싱과 슬라이싱 

colors = ['red', 'green', 'blue', 'pink', 'purple']

#indexing
for i in range(len(colors)):
    print(f'index: {i}')

#red, blue를 인덱스를 사용하여 조회하시오.
print(colors[0])
print(colors[2])


#purple를 인덱스를 사용하여 조회하시오.
print(colors[-1])


#리스트 생성
lst = [1,2,3]

#수정 
lst[0] = 'a'
print(lst)

lst[2] = lst[1] * 2
print(lst)

lst[1] = lst[0] * lst[2]
print(lst)
