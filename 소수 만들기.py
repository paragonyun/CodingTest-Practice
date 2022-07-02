from itertools import * ## itertools의 combinations 활용

def prime(a) : ## 판단하는 함수 생성
    for i in range(2,a) :
        if a % i == 0 :
            return False
        
    return True
 
    ## 원래 for문으로 내부에서 구현하려고 했는데 복잡해서.. 함수가 편해보였음

def solution(nums):
    comb = combinations(nums, 3)
    
    answer = 0 
    for i in comb : ## 이 조합들을 돌면서..
        
        num_sum = sum(i)  ## 그 수를 합한 뒤에
        
        if prime(num_sum)  == True :
            answer += 1
     
        else :
            continue

    return answer

## 배운 점 1 : itertools의 존재, 경우의 수 = itertools 쓰자! 
## 배운 점 2 : 소수 판별하는 함수 