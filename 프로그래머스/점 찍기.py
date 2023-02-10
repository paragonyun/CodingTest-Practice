import math
"""반지름이 d인 원 내의 (정수,정수)의 좌표를 구해라 라는 문제랑 똑같을듯
근데 그냥 단순하게 다 탐색하면 오래 걸릴 거 같으니까 짱구를 굴려야됨(근데 난 짱구가 없는디..)
-> 반지름이 정수인 원의 갯수를 구해보자
"""
def solution(k, d):
    answer = 0
    
    for i in range(0, d+1, k): # k배수만큼 해서 비교해야 하니까 k만큼 간격을 두고 비교
        
        answer += int(math.sqrt(d**2 - i**2))//k + 1
    
    return answer