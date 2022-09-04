# from itertools import permutations

# def solution(numbers):
#     numbers = [str(i) for i in numbers]    
    
#     lst = [i for i in permutations(numbers)]
    
#     lst2 = [''.join(i) for i in lst]
    
    
#     return max(lst2)

def solution(numbers) :
    nums = [str(i) for idx, i in enumerate(numbers)]
    nums.sort(key = lambda x : x*3, reverse= True)
    
    if sum(numbers) == 0 :
        return '0'
    
    return ''.join(nums)
    
    
'''
이건 너무 아이디어 싸움인 거 같아서... 정답을 봐버렸다 ㅠㅠㅠ
'''