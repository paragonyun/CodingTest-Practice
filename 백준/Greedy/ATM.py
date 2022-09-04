'''
예제 입력
5
3 1 4 3 2
'''

## 시작 시간 : 16:17
## 종료 시간 : 16:22

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

nujeok = []

for idx, i in enumerate(lst) :
    summed = sum(lst[:idx+1])
    nujeok.append(summed)

print(sum(nujeok))