def solution(A,B):
    """그냥 최솟값 x 최댓값 하면 될 거 같아서 sorted 시키고 pop으로 뽑아 비교시켰다."""
    answer = 0
    A, B = sorted(A), sorted(B)
    
    for i in range(len(A)):
        min_A = A.pop(0)
        max_B = B.pop(-1)
        answer += min_A*max_B

    return answer