#json3.py
#파이썬 객체 -> 문자열 

import json

#json 문자열
member = {
    'user_id' : 'python',
    'user_name' : '일길동',
    'age' : '10',
    'email' : 'python@gmail.com' 
}

json_str = json.dumps(member, ensure_ascii=False)

print(type(json_str))

print(json_str)

#print(json_str["user_id"]) : error