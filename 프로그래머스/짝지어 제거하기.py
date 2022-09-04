
def solution(s):
    
    

    stack = []
    
    for i in s :
        if len(stack) == 0 :
            stack.append(i)
            
        elif stack[-1] == i :
            stack.pop()
            
        else :
            stack.append(i)
            
    if len(stack) == 0:
        return 1
    else :
        return 0


'''
stack 문제라는 말에서 힌트를 얻어 풀었다.

Stack 문제를 풀 때는 빈 list를 만들어 놓고 하나하나 쌓아가면서 
바로 직전 것과 비교해나가는 방식으로 푸는 것같다.
'''  