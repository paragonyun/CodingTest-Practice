def solution(s):
    
    if len(s) % 2 != 0 :
        answer = str(s[len(s)//2])
        
    else : 
        answer = str(s[len(s)//2-1:len(s)//2+1])
        
    return answer