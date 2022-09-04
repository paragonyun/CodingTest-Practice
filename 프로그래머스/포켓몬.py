import collections
def solution(nums):
    answer = 0
    
    ## dictionary로 각 포켓폰의 수를 세어줌
    dic = collections.Counter(nums)
    
    ## 뽑을 수 있는 수
    picked_num = len(nums)//2 
    
    if len(dic.keys()) > picked_num :
        answer = picked_num
        
    else : 
        answer = len(dic.keys())
        
    
    return answer