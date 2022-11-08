def solution(food):
    result = []
    
    for idx, num in enumerate(food) :
        if idx == 0 :
            continue
            
        iters = num // 2
        if iters == 0 :
            continue
        
        for i in range(iters) :
            result.append(idx)
    
    nexts = result[::-1]
    
    result.append(0)
    
    for i in nexts :
        result.append(i)
    
    
    return ''.join(str(s) for s in result)