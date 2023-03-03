n = int(input())

series = [input() for _ in range(n)]

def summing(x):
    result = 0
    for i in x:
        if i.isdigit():
            result += int(i)
    
    return result

series = sorted(series, key=lambda x: (len(x), summing(x), x))

for i in series:
    print(i)
