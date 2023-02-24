def solution(n):
    """for문을 몇개를 쓰든 일단 해결해보자는 생각으로 해봄"""
    cnt = 0
    
    for i in range(1, n+1):
        tot = 0
        for j in range(i, n+1):
            tot += j
            if tot == n:
                cnt += 1
                break
            # 갑자기 범위가 너무 넓은 거 같아서 이걸로 확 줄여봄 (원래는 효율성에서 시간초과)
            elif tot > n:
                break
            """근데 이거 한 줄 더 넣었다고 효율성까지 통과함... 이야.. """
    return cnt  

"""배운점 : 역시 효율성을 위해 방법을 바꾸기 전에 범위를 줄일 수 있는지 고민하는 게 중요한 거같다.
            생각해보면 저 한 줄로 굉장히 많은 범위를 안 봐도 되기 때문에 저거 하나만으로 좀 컸던 것같다.
"""