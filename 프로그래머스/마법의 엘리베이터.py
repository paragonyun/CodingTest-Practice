def solution(storey):
    answer = 0
    """딱 보자마자 거스름돈 주는 거랑 비슷하다고 생각했음
    1. 어차피 1의 자리 수를 0으로 만들어야 10, 100을 써서 빠르게 내려갈 수 있음
    2. 6789 -> 올림으로 / 1234 -> 내림으로 이걸 먼저 하고
    3. 그럼 20이든 2550이든 나오게 됨. 그 자리수도 마찬가지로 하나씩 하면 되지 않을까? 싶었음
    4. 다만 5인 경우는 양쪽 다 할 수 있는데, 무지성 올림이나 내림 하면 테케에서 다 틀려버림... Why? 내림으로 했으면 돌 하나 덜 쓸 수 있는 건데 올림하면 자리수가 올라가버리므로 돌을 하나 더 써버릴 수가 있기 때문. 이거까지 고려해야 함(여기서 시간을 너무 많이 먹음..)
    """
    for i in range(1, len(str(storey))+1):
        # 현재 자리 수
        now = int(str(storey)[-i])
        print(storey, now, str(storey)[:i])

        if now > 5:
            answer += (10-now) # 일단 마법의 돌을 10-one 개만큼 써야됨
            storey += now * 10**(i-1) # 자리수를 올려야 하므로 10의 i-1승만큼을 곱한 값을 더함

        elif now < 5:
            answer += now # 마법의 돌 now개를 써서 0으로 만듦 -> 여긴 storey올릴 필요 x 자리수마다 숫자 변화가 없기 때문

        elif now == 5: 
            if (storey // 10) % 10 > 4:
                storey += now * 10**(i-1)
            answer += now
            
    return answer
