n = input()

for i in range(1, int('F', 16)+1) :
    print(f'{n}*{hex(i)[2:].upper()}={hex(int(n, 16)*i)[2:].upper()}')