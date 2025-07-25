#list9.py
#리스트 함수에 대한 예제 프로그램입니다. 

lst = [1,2,3]


#lst[3] = 4 오류 발생

#요소 추가
lst.append(4)
print(lst)

#끝에 리스트, 튜플 등 하나씩 추가 
# lst.append([5, 6])
lst.extend([5,6])
print(lst)


#특정 위치에 추가 
lst.insert(1, 'b')
print(lst)
[1, 'b', 2, 3, 4, 5, 6]

#마지막 삭제
lst.pop()
print(lst)

#특정 값 삭제 
if 'b' in lst:
    lst.remove('b')
print(lst)

#모든 값 삭제 
lst.clear()
print(lst)