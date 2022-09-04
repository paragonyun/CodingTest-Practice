def solution(s):
    # if s.count('(') == s.count(')') :
    #     if s[0] == '(' and s[-1] == ')':
    #         return True
    #     else :
    #         return False
    # else :
    #     return False
    
    stack = []
    
    for i in s :
        if i == '(' :
            stack.append(i)
        
        else :
            if len(stack) == 0:
                return False
            
            else :
                stack.pop() ## 웃긴 게 이거 pop(0)으로 하면 효율성 빠꾸나고 pop()으로 하면 안 남ㅋㅋㅋ
                
    if len(stack) != 0 :
        return False
    
    return True
        
        
'''
Stack 문제였다. 그냥 주석 처리된 방식으로 풀게되면 "())(()" 이런 케이스를 넘기게 된다.
따라서 하나하나 쌓아가는 Stack 알고리즘을 사용했어야 했는데, 하나하나 쌓아가다가 
'(' 면 일단 넣고 ')'가 "탐지"(넣은 거 아님) 이미 (가 있으면 들어왔던 (를 뺀다. 그런 식으로 빼면 정상적으로는
stack은 빈 칸이 되어야 한다. 
아니면 잘못됐다는 것이므로 return False
'''
    