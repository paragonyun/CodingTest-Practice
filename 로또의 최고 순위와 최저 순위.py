def solution(lottos, win_nums):
    answer = []
    # 맞춘 거
    correct = set(win_nums)&set(lottos)

    zeros = lottos.count(0) # 가능성 있는 거의 갯수    

    rank_high = 7 - (len(correct)+zeros)
    rank_low = 7-len(correct)
    
    if rank_high>6 :
        rank_high=6

    if rank_low >=6 :
        rank_low = 6
    
    answer.append(rank_high)
    answer.append(rank_low)
    
    return answer