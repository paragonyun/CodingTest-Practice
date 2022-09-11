n = int(input())

loc = []

for i in range(n) :
    loc.append(tuple(map(int, input().split())))

maps = [[0]*19 for i in range(19)]

while loc :
    now_loc = loc.pop()
    x, y = now_loc[0], now_loc[1]

    maps[x-1][y-1] = 1

for i in maps :
    for j in i :
        print(j, end=' ')
    print('')