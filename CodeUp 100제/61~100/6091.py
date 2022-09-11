a, b, c = map(int, input().split())

x = 1
while x%a != 0 or x%b!=0 or x%c !=0 :
    x += 1
print(x)