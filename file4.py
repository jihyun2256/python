#file4.py
#'서시.txt' 파일에서 1라인씩 읽어서 출력하는 예제 프로그램입니다. 



try: 
    #1. file 열기 
    with open('서시.txt', 'r', encoding='utf-8') as file:
    #2. file 읽기: list
        lines = file.readlines()

        num = 1
        for line in lines:
            print(f'{num} : {line.strip()}')
            num += 1

except Exception as err:
    print(f'err : {err}')

print('end')
