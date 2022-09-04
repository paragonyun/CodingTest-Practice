def solution(board, moves):
    answer = 0
    '''
    [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]]
    '''
    
    poped =[]
    
    
    for move in moves :
        for idx,row in enumerate(board) :
            if row[move-1] == 0 :
                continue ## 비어있으면 다음 row로 넘어가기
            elif row[move-1] != 0 :
                poped.append(row[move-1])
                board[idx][move-1] = 0 ## 뽑혔으니까 이제 0으로 만들어줘야됨!!!!!!! 
                break ## 다음 move로 이동

        if len(poped)>=2 and poped[-1]==poped[-2] : ## 아예 그냥 추가 될 때마다 고려하는 게 편할듯
            poped.pop(-1)
            poped.pop(-1)
            
            answer += 2
    
    return answer