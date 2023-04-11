## 시간초과
# def solution(sequence, k):
    # answer = []
    
#     candidates = []
    
#     for i in range(len(sequence)): # 첫번째 idx
#         for j in range(i, len(sequence)): # 두번째 idx
#             lst_sum = sum(sequence[i:j+1])
            
#             if lst_sum == k:
#                 candidates.append((i, j, j-i)) # 시작 idx, 끝 idx, 길이 정보를 담은 tuple append
                
#     answer = sorted(candidates, key= lambda x: (x[2], x[0])) # 길이 기준 sorting
                    
#     return answer[0][:2]

def solution(sequence, k):
    """투포인터를 이용한 풀이로 해보자"""
    
def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0

    res = []
    for i in range(n): # n만큼 돌면서... 

        while max_sum < k and end < n: # max_sum -> 누적합 => 누적합이 k가 되기 전이면서 end point가 n미만일 때까지
            max_sum += sequence[end]   # 누적합 계산부분
            end += 1                   # end point 1씩 증가

        if max_sum == k:               # 그러다 누적합이 k면 
            res.append([i, end-1, end-1-i])  # i(start point), end-1, end-1-i 정보 append

        max_sum -= sequence[i]         # 누적합에서 현재값을 빼줌으로써 초기화
        

    answer = sorted(res, key= lambda x: (x[2], x[0])) # 길이 기준 sorting
                    
    return answer[0][:2]

"""
투포인터와 누적합의 개념을 알 수 있었다.
한번 잘 익혀두면, 경우의 수 따질 때 매우 좋을 거 같았다.
"""