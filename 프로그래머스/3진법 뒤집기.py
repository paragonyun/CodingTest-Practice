def solution(n):
    answer =''
    while n :
        n, mod = divmod(n, 3) 
        answer += str(mod) # 이거 자체로 거꾸로 뒤집은 게 나옴

    return int(answer, base= 3)