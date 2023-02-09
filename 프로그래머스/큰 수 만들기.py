def solution(number, k) :

    number = list(number)
    
    stack = []
    for i in number:
        if len(stack) == 0: # stack이 비어 있는 경우
            stack.append(i) # 추가하고
            continue        # 다음으로 넘어감
            
        elif k > 0:
            while stack[-1] < i :# 가장 마지막에 있는 stack이 현재 숫자보다 작은 한 계속 반복
                stack.pop() # 원래 있던 걸 빼고
                k -= 1      # k - 1 해줌 이 k는 pop을 수행할 수 있는 기회라고 생각하면 편함
                if len(stack) == 0 or k == 0 : # k==0이 되는 경우엔..
                    break
                    
        # 그러다가 큰 게 나오면 그걸 넣어주면 됨
        stack.append(i)
    
    if k > 0 : # 다 돌았는데 여전히 k가 남아있는 경우가 있을 거임
        stack = stack[:-k] #그럼 상위 k개까지만 표시
    
    return "".join(stack)