# 시간초과
# def solution(people, limit):
#     answer = 0
#     people = sorted(people, reverse=True)
    
#     while people:
#         if len(people) == 1:
#             answer += 1
#             return answer 
#         now = people.pop(0) # 가장 무거운 사람
        
#         if now + people[-1] <= limit: # 가장 무거운 사람 + 가장 가벼운 사람이 limit을 안 넘기면
#             people.pop(-1)
#             answer += 1
#         elif now + people[-1] > limit: # 제한을 넘기면
#             answer += 1
        
#     return answer
"""시간초과 = deque 써보기..!
다 똑같은데 deque쓰니까 효율성도 바로 통과했다. 역시... 안 되면 일단 트라이 해보는 게 좋은 거 같다
"""

from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse=True))
    
    while people:
        if len(people) == 1:
            answer += 1
            return answer 
        now = people.popleft() # 가장 무거운 사람
        
        if now + people[-1] <= limit: # 가장 무거운 사람 + 가장 가벼운 사람이 limit을 안 넘기면
            people.pop()
            answer += 1
        elif now + people[-1] > limit: # 제한을 넘기면
            answer += 1
        
    return answer
