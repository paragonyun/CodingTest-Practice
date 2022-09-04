def solution(n):    
    n_ =  bin(n)[2:].count('1')
    
    while True :
        n += 1
        if bin(n)[2:].count('1') == n_ :
            return n

'''
bin 함수와 count 함수를 알고 있었다면 쉽게 풀렸던 문제
'''