"""
정말 문제 그대로 풀었음
자세한 설명은 주석에!
"""
from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    # Case2 처럼 아예 없는 경우엔 그냥 0 return 
    for i in want:
        if i not in discount:
            return 0
    
    # Sliding Window를 해가면서 비교
    for i in range(len(discount)):
        now = discount[i:i+10] # 10일치를 볼 거기 때문에 i+10
        if len(now) != 10:     # 해당 window의 길이가 10이 안 되면 그냥 멈춤 (이거 안 하면 9,8,7,6,, 인 경우까지 다 해버림)
            break
        
        # 먼저 원하는 상품이 다 있는지 확인
        if (len(set(now) - set(want)) == 0) & (len(set(want) - set(now)) == 0): # set을 해서 각 차집합의 수가 똑같이 0이어야 두 리스트의 요소가 모두 같다고 할 수 있음 (이거 개선 가능할 거 같은데,,, 모르겠네요)
            
            # 상품이 다 있는 경우 이제 원하는 만큼 있는지 확인
            cnts = Counter(now) # from collections import Counter 활용
            check = 0           # 각 상품마다 개수가 충족하는지 check
            for idx, w in enumerate(want): # 상품을 돌면서...
                if cnts[w] == number[idx]: # w상품의 개수가 number[idx]와 같으면
                    check += 1             # check에 +1을 해줌
                    
                if check == len(number):   # 그 check의 길이가 number의 길이와 같으면 상품의 개수까지 충족한다는 걸 의미
                    answer += 1            # 뿌라스

    return answer