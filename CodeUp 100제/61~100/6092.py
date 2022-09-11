n = int(input())
lst = list(map(int, input().split()))


dic = {}
for i in range(1, 24) :
    dic[i] = 0

for i in lst :
    dic[i] += 1

for i in range(1, 24) :
    print(dic[i], end = ' ')