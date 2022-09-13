w, h = map(int, input().split())

maps = [[0]*h for i in range(w)]


n_bars = int(input())

for i in range(n_bars) :
    l, d, x, y = map(int, input().split())

    if d == 0 :
        for length in range(l) :
            maps[x-1][y-1+length] = 1
        
    else :
        for length in range(l) :
            maps[x-1+length][y-1] = 1

for rows in maps :
    for cols in rows :
        print(cols, end=' ')
    print()