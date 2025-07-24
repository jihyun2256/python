#exam3_2.py
#1부터 100가지의 합을 계산하는 프로그램

total = 0 #변수 할당 꼭 해야함 

for i in range(1, 101, 1):
    total += i #누적하기 

print(f'1부터 100까지의 합은 : {total}')