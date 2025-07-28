#file2.py
#'서시.txt' 파일에서 1라인씩 읽어서 출력하는 예제 프로그램입니다. 

file = None

try: 
    #1. file 열기 
    file = open('서시.txt', 'r', encoding='utf-8')
    #2. file 읽기: list
    lines = file.readlines()

    for line in lines:
        print(line.strip())

except Exception as err:
    print(f'err : {err}')
finally:
    if file is not None:
        #3.파일 리소스 해제 
        file.close()

print('end')
