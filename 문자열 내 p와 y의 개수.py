from collections import Counter
def solution(s):
    
    a = Counter(s.lower())
    if a['p'] == a['y'] : 
        return True
    else : 
        return False
'''
collections 의 Counter 사용
'''