#continue3.py

# 학생들의 성적이 리스트 자료로 있다. 성적을 체크해서 합격한 학생의결과만 출력하는 프로그램. 60점 이상합격(continue문 사용)
# 예) scores = [ 90, 88, 34, 56, 67, 78, 88, 60, 59, 100 ]
#  1번 학생축하합니다. 합격입니다.
#  2번 학생축하합니다. 합격입니다. 
#  5번 학생축하합니다. 합격입니다.
#  6번 학생축하합니다. 합격입니다. 
#  7번 학생축하합니다. 합격입니다.
#  8번 학생축하합니다. 합격입니다. 
# 10번 학생 축하합니다. 합격입니다.

scores = [ 90, 88, 34, 56, 67, 78, 88, 60, 59, 100 ]

#print(len(scores))

# for i in range(0, len(scores), 1): #range(0, len(scores), 1)
#     if scores[i] < 60:
#         continue

#     print(f'{i+ 1}번 학생 축하합니다. 합격입니다.')


for i in range(len(scores)): #range(0, len(scores), 1)
    if scores[i] < 60:
        print(f'{i+ 1}번 학생 축하합니다. 합격입니다.')
    
    
