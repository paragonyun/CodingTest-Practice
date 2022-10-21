from itertools import combinations

def solution(number):
    cnt = 0
    
    lst = combinations(number, 3)
    for i in lst :
        if sum(i) == 0 :
            cnt += 1
        else :
            continue
    
    return cnt