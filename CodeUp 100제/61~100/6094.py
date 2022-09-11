import heapq

n = int(input())
lst = list(map(int, input().split()))

heapq.heapify(lst)

print(heapq.heappop(lst))