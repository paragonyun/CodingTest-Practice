r, g, b = map(int, input().split())

cnt = 0
for first in range(r) :
    for second in range(g) :
        for third in range(b) :
            print(first, second, third)
            cnt +=1

print(cnt)