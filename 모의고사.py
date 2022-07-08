def solution(answers):
    
    best = []
    
    rank = {1 : 0,
           2 : 0,
           3 : 0}
    
    no1 = [i for i in range(1,6)] * len(answers)
    no1 = no1[:len(answers)]

    no2 = [2,1,2,3,2,4,2,5] * len(answers)
    no2 = no2[:len(answers)]
    
    no3 = [3,3,1,1,2,2,4,4,5,5] * len(answers)
    no3 = no3[:len(answers)]
    

    
    lst = [no1, no2, no3]
    for iidx, i in enumerate(lst) :
        cor_num = 0
        for idx, j in enumerate(i) :
            if j == answers[idx] :
                cor_num += 1
                
            else : 
                continue
                
        rank[iidx+1] = cor_num
    
    best = [k for k, v in rank.items() if max(rank.values()) == v]
    
    return best

'''
배운 것 
- dictionary에서 value의 최댓값으로 찾기
'''