# 시간초과
# def solution(topping):
#     answer = 0
    
#     n = len(topping)
    
#     for i in range(1, n):
#         lst_1 = len(set(topping[i:]))
#         lst_2 = len(set(topping[:i]))
        
#         if lst_1 == lst_2:
#             answer += 1
    
#     return answer
from collections import Counter
def solution(topping):
    answer = 0
    n = len(topping)
    cnts = Counter(topping) # Counter는 없는 key를 indexing하면 0을 return 한다. -> 다 빼면 남아있어서 나중에 del로 삭제해줘야한다.
    
    other = {}

    for i in range(n): 
                
        if topping[i] not in other : # 값이 other에 없으면 
            other[topping[i]] = 1    # other dictionary의 i번째 토핑 key값에 줬다고 설정
            
        elif topping[i] in other :   # 이미 있으면
            other[topping[i]] += 1   # 추가
        
        cnts[topping[i]] -= 1 # i번째 topping을 뺌 (1개만)

        if cnts[topping[i]] == 0 : # 다 줬으면 dictionary에서 key 삭제
            del cnts[topping[i]]
        
        ## 위에꺼대로 주면서 동시에 dictionary끼리의 길이를 비교함
        if len(cnts) == len(other):
            answer += 1
        
    return answer