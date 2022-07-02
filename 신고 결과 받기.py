def solution(id_list, report, k):
    answer = []
    
    ed_dict = {}  # 신고 당한 사람 : 횟수 dict
    er_dict = {}  # 신고 한 사람 : 당한사람 dict
    for i in id_list :
        ed_dict[i] = 0
        er_dict[i] = []
    

    
    
    for i in set(report) :
        er, ed = i.split() # 신고한 사람, 신고당한 사람
        
        er_dict[er].append(ed) # 한 사람 -> 당한사람 리스트에 추가
        
        
        ed_dict[ed] += 1 # 당하면 +1
    

    
    for i in id_list :
        cnt = 0
        for j in er_dict[i] :
            if ed_dict[j] >= k :
                cnt += 1
        answer.append(cnt)    
    
    return answer