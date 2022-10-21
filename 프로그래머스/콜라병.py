def solution(a, b, n):
    bottle = 0
    
    while n >= a :
        if n < 2 :
            break
            
        get = (n//a)*b 
        n = n - (n-(n%a)) + get 
        bottle += get
        
    return bottle