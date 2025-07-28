


#함수 정의 
def is_valid_signup(input_id, input_pw):

    special_word = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '?']
    
    if len(input_id) < 10:
        return "아이디는 반드시 10자 이상이어야 합니다."
    
    if len(input_pw) <8 or len(input_pw) > 16:
        return "패드워드는 반드시 8~16자리 사이여야 합니다."

    if input_id in input_pw:
        return "패스워드에 아이디가 포함되면 안됩니다."
    
    if not any(ch in special_word for ch in input_pw):
        return "패스워드에는 다음의 특수 문자가 반드시 하나 이상 포함되어야 합니다."
    
    return "회원가입이 성공적으로 이루어졌습니다."
   
    
#사용자로부터 아이디와 비밀번호를 입력 받아서 유효성을 체크합니다.
input_id = input('아이디를 입력하세요')
input_pw = input('비밀번호를 입력하세요')

print(is_valid_signup(input_id, input_pw))