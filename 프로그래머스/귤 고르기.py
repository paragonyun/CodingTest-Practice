from collections import Counter
def solution(k, tangerine):
    answer = 0
    
    counts = Counter(tangerine) # {크기 : 개수}
    
    for key, v in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            break
        
    return answer

"""
Counter 모듈로 크기 별 개수를 dictionary로 만들고 value를 기준으로 sorting
k개에서 value를 빼면 k를 도는 만큼 다른 개수의 크기가 된다는 것이 되므로 그렇게 함
"""