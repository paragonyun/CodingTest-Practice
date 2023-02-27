# from collections import deque
# def solution(numbers):
    
#     result = deque(numbers)
#     for i in range(len(numbers)):
#         result.append(-1)
#         for j in numbers[i+1:]:
#             if i < j:
#                 result.pop()
#                 result.append(j)
#                 break
#     answer = 0
#     return answer

# def solution(numbers):
#     answer = []
    
#     for i in range(len(numbers)):
#         answer.append(-1)
#         for j in numbers[i+1:]:    
#             if numbers[i] < j:
#                 answer.pop(-1)
#                 answer.append(j)
#                 break
                
#     return answer
# def solution(numbers):
#     answer = []
    
#     for i in range(len(numbers)):
#         answer.append(-1)
#         if max(numbers) < numbers[i]:
#             continue
        
#         for j in numbers[i+1:]:    
#             if numbers[i] < j:
#                 answer.pop(-1)
#                 answer.append(j)
#                 break
                
#     return answer

"""계속해서 시간 초과가 뜬다..."""
def solution(numbers):
    answer = [-1]*(len(numbers)) # -1로 일단 채워줌
    stack = []
    for i in range(len(numbers)): # numbers의 index를 돌면서
        while stack and numbers[stack[-1]] < numbers[i]: # stack이 비어있지 않고 numbers의 i번째 index보다 stack의 최신 index(이전 꺼)가 크면... 
            answer[stack.pop()] = numbers[i]
        stack.append(i) # 처음일 땐 그냥 0을 넣는 용도고, 나중에 가면 stack의 index를 모아두는 용도가 됨
    return answer