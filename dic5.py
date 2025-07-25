#dic5.py
#리스트 안에 딕셔너리

member_list = [
    {'user_name' : '일길동',
    'age' : 10,
    'email': 'python@gmail.com'},

    {'user_name' : '이길동',
    'age' : 20,
    'email': 'python@gmail.com'},

    {'user_name' : '삼길동',
    'age' : 30,
    'email': 'python@gmail.com'}
]

for member in member_list:
    user_name = member['user_name']
    age = member['age']
    email = member['email']
    print(f'{user_name}, {age}, {email}')