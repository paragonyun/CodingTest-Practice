from itertools import permutations

def solution(k, dungeons):
    
    lst = permutations(dungeons)
    
    cnt_lst = []
    
    for i in lst :
        
        k_t = k
        
        cnt = 0
        
        for a, b in i :
            
            if k_t < a : 
                cnt_lst.append(cnt)
                break
            
            elif k_t >= a :
                cnt += 1
                k_t -= b
                
        if cnt == len(dungeons) :
            cnt_lst.append(cnt)               
        
    return max(cnt_lst)

'''
완전 탐색 문제.. permutation 을 이용하면 쉽게 풀리는 문제였다.
'''