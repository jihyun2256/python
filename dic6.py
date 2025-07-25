#dic6.py
#딕셔너리 안에 딕셔너리 

dd = {
    'Park': {'age':25, 'blood': 'B'},
    'Kim': {'age':30, 'blood': 'A'},
    'Han': {'age':28, 'blood': 'AB'},
}

#name에 key 저장 
for name in dd:
    print(name, dd[name]['age'], dd[name]['blood'])