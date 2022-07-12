def solution(left, right):
    answer = 0
    for i in range(left, right+1) :
        if len([x for x in range(1,i+1) if i % x == 0]) %2 == 0 : ## 약수의 수가 짝수면
            answer += i
        else :
            answer -= i
    return answer