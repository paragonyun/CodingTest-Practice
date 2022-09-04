def solution(arr, divisor):
    answer = sorted([i for i in arr if i % divisor == 0])
    if len(answer) == 0 :
        return [-1]

    return answer 

def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]