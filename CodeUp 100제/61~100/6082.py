n = int(input())

for i in range(1, n+1) :
    for j in str(i) :
        if j == '3' :
            i = 'X'
            break
        elif j == '6' :
            i = 'X'
            break
        elif j == '9' :
            i = 'X'
            break

    print(i, end=' ')
