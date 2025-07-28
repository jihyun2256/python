#json2.py
#문자열 -> 파이썬 객체 
#파이썬 객체 -> 문자열 

import json

#json 문자열
member_str = '{"user_id" : "python", "user_name" : "일길동","age" : "10","email" : "python@gmail.com"}'

_dict = json.loads(member_str)

print(type(_dict))
print(_dict)

#user_id와 user_name만 출력 
print(f'user_id : {_dict["user_id"]}')
print(f'user_name : {_dict["user_name"]}')

for key, value in _dict.items():
    print(f'{key} : {value}')