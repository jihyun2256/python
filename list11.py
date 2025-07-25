#list11.py
#리스트 함수에 대한 예제 프로그램입니다.

colors = ['yellow', 'green', 'blue', 'yellow']

#일치하는 값의 인덱스 번호를 반환 
print(colors.index('yellow'))
print(colors.index('yellow', 1)) 

num_list = [1, 3, 2]

#모든 값을 뒤집어 나열 
num_list.reverse()
print(num_list)

#오름차순 정렬 
num_list.sort()
print(num_list)

#내림차순 정렬
num_list.sort(reverse=True)
print(num_list)