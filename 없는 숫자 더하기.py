def solution(numbers):
    
    ran = set(range(10))
    
    answer = sum(ran - set(numbers)) 
    
    return answer