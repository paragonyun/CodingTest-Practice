def solution(n, m, section):
    answer = 0
    paint_start = section[0] - 1    
    
    for i in section:
        if paint_start < i:
            paint_start = i + m -1 # 이 만큼을 칠함
            answer += 1
    
    return answer