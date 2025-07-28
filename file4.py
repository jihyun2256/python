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


# 1 : 
# 2 : 죽는 날까지 하늘을 우러러
# 3 : 한 점 부끄럼이 없기를,
# 4 : 잎새에 이는 바람에도
# 5 : 나는 괴로워했다.
# 6 : 별을 노래하는 마음으로
# 7 : 모든 죽어 가는 것을 사랑해야지
# 8 : 그리고 나한테 주어진 길을
# 9 : 걸어가야겠다.
# 10 :
# 11 : 오늘 밤에도 별이 바람에 스치운다.
# end