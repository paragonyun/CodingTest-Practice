def solution(priorities, location):
    
    cnt = 0
    
    priorities = [(idx, i) for idx, i in enumerate(priorities)]

    while True:
    
        idx,  first = priorities.pop(0) ## 가장 앞에 하나 객체로 만듦

        if len(priorities) != 0 :
            now = [value for idx, value in priorities]
            max_value = max(now)
        
        if (max_value <= first): 
            cnt += 1
            
            if location == idx :
                return cnt
            
        else :
            priorities.append((idx, first))
    else :
        cnt += 1
        return cnt