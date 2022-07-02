def solution(numbers, hand):
    dic = {
        ## 번호마다 좌표를 만듦
        '*' : (-1,0),
        '#' : (1,0),
        1 : (-1,3),
        2 : (0,3),
        3 : (1,3),
        4 : (-1,2),
        5 : (0,2),
        6 : (1,2),
        7 : (-1,1),
        8 : (0,1),
        9 : (1,1),
        0 : (0,0), 
    }
    result = []
    L_loc = dic['*']
    R_loc = dic['#']
    
    for i in numbers :         
        if i in [1,4,7,'*'] :
            result.append("L")
            L_loc = dic[i]
            
        elif i in [3,6,9,'#'] :
            result.append("R")
            R_loc = dic[i]
            
        elif i in [2,5,8,0] :
            ## 여기부터 거리계산
            L_distance = abs(dic[i][0] - L_loc[0]) + abs(dic[i][1] - L_loc[1])
            R_distance = abs(dic[i][0] - R_loc[0]) + abs(dic[i][1] - R_loc[1])
            
            
            ## 오른손이 왼손보다 더 멀리 있으면
            if R_distance > L_distance : 
                result.append("L") # 왼손으로 누르고
                L_loc = dic[i] # 좌표 바꿔줌
            
            ## 왼손이 오른손보다 멀리 있으면
            elif R_distance < L_distance : 
                result.append("R") # 오른손으로 누르고
                R_loc = dic[i] # 좌표 바꿔줌
                
            elif R_distance == L_distance :
                if hand == 'right' :
                    result.append("R") # 오른손으로 누르고
                    R_loc = dic[i] # 좌표 바꿔줌  
                
                else : 
                    result.append("L") # 왼손으로 누르고
                    L_loc = dic[i] # 좌표 바꿔줌
            
    answer = "".join(result)

    return answer