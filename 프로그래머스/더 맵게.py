import heapq
def solution(scoville, K):
## 시간 초과
#     cnt = 0
    
#     while True :
#         scoville = sorted(scoville)
        
#         new = scoville.pop(0) + scoville.pop(1)*2
        
#         scoville.append(new)
        
#         cnt += 1
        
#         if min(scoville) >= K :
#             return cnt 
        
#         elif len(scoville) == 1 :
#             return -1

    ## heapq 사용
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        new =  heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        
        heapq.heappush(scoville, new)
        
        cnt += 1
        
        if scoville[0] >= K :
            return cnt
        
        elif len(scoville) == 1 :
            return -1
        
'''
heapq의 필요성을 깨달았다.
list의 정렬을 다루는 문제에서 효율성을 따진다면
거의 무조건 heapq를 떠올려야할듯
'''
        
        