# from collections import defaultdict

# def solution(numbers, target):
    

    
#     gra = defaultdict(list)
#     for i in range(len(numbers)) :
#         gra[i] = [numbers[i], numbers[i]*(-1)]
    
#     visited = []
#     stack = gra[0]    
    
#     while stack :

#         n = stack.pop()
        
#         if n not in visited :
#             visited.append(n)
#             stack += gra[n] - set(visited)
    
#     return True
    
    
#     return answer

from itertools import product
import numpy as np

def solution(numbers, target):
    pm = [-1,1]
    a = product(pm, repeat = len(numbers))
    
    cnt = 0
    
    for i in a :
        result = np.array(numbers) * np.array(i)
        if sum(result) == target :
            cnt += 1
    
    return cnt

''' 
다시 풀어봐야할 것같다... 풀리긴 하는데 시간이 너무 오래 걸려
'''