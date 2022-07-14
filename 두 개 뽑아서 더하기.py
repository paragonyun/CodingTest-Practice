import itertools
def solution(numbers):
    answer = []
    
    combs = itertools.combinations(numbers ,2)
    
    for i in combs :
        answer.append(sum(i))
    
    return sorted(list(set(answer)))    

'''
itertools의 존재는 항상 기억하고 있자.
경우의 수 = itertools !!!!
'''