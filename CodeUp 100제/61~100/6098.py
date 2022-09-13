maps = [list(map(int, input().split())) for i in range(10)]

x, y = 1, 1

while True :
    if maps[x][y] == 2 :
        maps[x][y] = 9
        break

    maps[x][y] = 9
    
    n_x = x+1
    n_y = y+1

    if maps[x][n_y] == 0 or maps[x][n_y] == 2:
        y = n_y
        continue
    
    elif maps[x][n_y] == 1 :
        if maps[n_x][y] == 1:
            break
        else :
            x = n_x
            continue

for rows in maps :
    for cols in rows :
        print(cols, end=' ')
    print()