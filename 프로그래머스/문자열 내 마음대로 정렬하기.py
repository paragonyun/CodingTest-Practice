def solution(strings, n):
    return sorted(strings , key = lambda x : (x[n], x))


'''
sorted, sort의 key = 의 존재, key와 lambda로 정렬 기준을 "여러개" 세울 수 있다는 것
'''