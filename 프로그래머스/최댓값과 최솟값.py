def solution(s):
    
    lst = list(map(int, s.split()))
    
    return str(min(lst)) + " " + str(max(lst)) 

"""map 함수와 split함수를 아는지 모르는지를 물어봤던 문제"""