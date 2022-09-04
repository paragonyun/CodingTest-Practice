def solution(citations):

    citations = sorted(citations, reverse=True) 
    
    for idx, i in enumerate(citations) :
        if idx >= i :
            return idx
        
    return len(citations)

    '''
    문제를 이해하는 거 자체가 어려웠다 말을 무슨 그렇게 하는지...
    내림차순으로 정렬해서 idx와 그 값을 비교하면 자연스레 수를 비교하는 게 된다. (idx가 내림차순으로 되어있으므로)
    idx가 i 보다 크거나 같은 첫번째 조건만 만족하면, 두번째 조건은 자동으로 충족되므로 바로 idx 를 return 한다.
    '''