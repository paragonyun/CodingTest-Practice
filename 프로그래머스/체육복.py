def solution(n, lost, reserve):
    answer = 0
    
    ## reserve가 lost에 있을 수도 있음 -> 체육복을 빌려줄 수 없으니 reserve와 lost 둘 다에서 빠져야 됨
    re_reserve = [i for i in reserve if i not in lost]
    re_lost = [i for i in lost if i not in reserve]
    
    ## index로 풀 거기 때문에 sorting 해줘야됨
    re_reserve.sort()
    re_lost.sort()
    
    ## 일단 기본적으로 n-len(re_lost) 만큼 체육복이 있음
    answer = n - len(re_lost)
    
    for idx, i in enumerate(re_lost) :
        if re_lost[idx]-1 in re_reserve :
            answer += 1
            re_reserve.remove(re_lost[idx]-1)

        elif re_lost[idx] + 1 in re_reserve :
            answer += 1
            re_reserve.remove(re_lost[idx]+1)
            
    
    
    return answer

    ##이런 것을 Greedy 알고리즘이라고 한다
    ## Greedy 알고리즘은 "현재" 상태에서 가장 좋은 것을 고르는 알고리즘으로
    ## 미래의 보상을 고려하지 않는다.