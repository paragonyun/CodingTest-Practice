def solution(num):
    i = 0
    
    if num == 1:
        return 0
    
    while i <= 500 :
        if num % 2 == 0 :
            num /= 2
            
        elif num % 2 != 0 :
            num = 3*num + 1
            
        i += 1
        
        if num == 1 :
            return i
        
    return -1