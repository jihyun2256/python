#file5.py
#'car_fleet.csv' 파일의 내용을 읽어서 출력하는 예제 프로그램입니다.


import csv

try :
    with open('car_fleet.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        #헤더 정보 출력하지 않으려면
        next(reader)
        for row in reader:
            #print(row)
            print(f'{row[0]}, {row[1]}, {row[2]}')

except Exception as err:
    print(f'err : {err}')