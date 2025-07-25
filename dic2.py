#dic2.py

member = {
    'user_name' : '일길동',
    'age' : 10,
    'email': 'python@gmail.com'
}

#이름과 나이, 이메일 정보를 출력하시오.
print(member['user_name'], member['age'], member['email'])


#이름을 '홍길동' 으로 변경하시오.
member['user_name'] = '홍길동'
print(member)