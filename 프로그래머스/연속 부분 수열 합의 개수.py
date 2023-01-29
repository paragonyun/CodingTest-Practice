def solution(elements):
    """순서를 지키면서 봐야하기 때문에 단순 itertools 쓰면 안 됨"""
    
    total = []
    double_elements = elements*2
    
    for i in range(len(elements)): # 0, 1, 2, 3, 4 ...
        for j in range(len(elements)): # 0, 1, 2, 3, 4 ...
            # [0:1] , [1:3], [2:4] ... 
            total.append(sum(double_elements[j : j+i+1]))
        
    return len(set(total))