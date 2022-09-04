import numpy as np
import math

# def solution(progresses, speeds):
    
#     answer = []

#     d_days = (100-np.array(progresses)) / speeds 
    
#     d_days = [math.ceil(i) for i in d_days]
    
#     day = 1
    
#     standard = d_days[0]
    
#     print(d_days)
    
#     for idx, i in enumerate(d_days[1:]) :
        
#         if standard >= i :
#             day += 1
            
#         elif standard < i :
#             answer.append(day)
#             day = 1
#             standard = d_days[idx]
            
#         if idx == len(d_days)-2 :
#             answer.append(day)
            
#             return answer
            

def solution(progresses, speeds):
    answer = []
    day = 1
    d_days = (100-np.array(progresses)) / speeds
    d_days = [math.ceil(i) for i in d_days]
    
    standard = d_days.pop(0)
    
    while True :
#         if len(d_days) == 0 :
        
        now = d_days.pop(0)
        
        if standard >= now :
            day += 1
            
        elif standard < now :
            answer.append(day) 
            day = 1
            standard = now
        
        if len(d_days) == 0 :
            answer.append(day)
            return answer

        
'''
나는 같은 알고리즘을 for 문 vs while+pop 으로 해본 것뿐인데 while+pop은 풀렸다...
왜지? 테스트 케이스에서 이상한 게 있었나보다...
'''

