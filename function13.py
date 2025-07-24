#function13.py
#언패킹에 대한 예제 프로그램 입니다. 

def print_all(*args):
    print(args)


_list = [1, 2, 3]

print_all(*_list)  # print_all(1, 2, 3) : 언패킹  


_list = [1, 2, 3, 4]

print_all(*_list)  # print_all(1, 2, 3) : 언패킹  
