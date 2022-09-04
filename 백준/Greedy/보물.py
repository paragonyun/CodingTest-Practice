'''
입력 예시 
5
1 1 1 6 0
2 7 8 3 1

3
1 1 3
10 30 20

9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1
'''

## 시작 시간 : 16:25
## 종료 시간 : 17:00

# from itertools import permutations

# N = int(input())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# sum_lst = []

# for i in permutations(A,N) :
#     sum_1 = []
#     for idx, ele in enumerate(i) :
#         sum_1.append(ele*B[idx])
    
#     sum_lst.append(sum(sum_1))

# print(min(sum_lst))

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []

for i in range(N) :
    ele = min(A)*max(B)
    result.append(ele)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(sum(result))