# def solution(k, m, score):
#     score = sorted(score, reverse=True)
#     sumu = 0
    
#     while score :
#         if len(score) < m :
#             break
            
#         temp_lst = score[:m]
#         score = score[m:]
        
#         sumu += min(temp_lst) * m
    
#     return sumu

from collections import deque 
def solution(k, m, score) :
    score = deque(sorted(score, reverse=True))
    fin = 0
    
    while score :
        if len(score) < m :
            break
        
        temp_lst = []
        
        for i in range(m) :
            
            temp = score.popleft()
            temp_lst.append(temp)
            
            if len(score) == 0 :
                break
    
        fin += min(temp_lst) * m

    return fin

'''
deque의 속도를 체감할 수 있었다.

역시 정렬로 해서 엔간히 안 되면 그냥 deque가 답이다
'''