import numpy as np
def solution(absolutes, signs):
    
    booho = []
    
    for i in signs :
        if i == True :
            booho.append(1)
            
        elif i == False :
            booho.append(-1)
            
    answer = sum(np.array(absolutes).T * np.array(booho)).tolist()
    
    return answer