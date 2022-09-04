def solution(s):
    answer =''
    for i in sorted(s)[::-1] : 
        answer += i
    return answer