import math

def solution(n, m):
    answer = []
    answer.append(math.gcd(n,m))
    answer.append(n*m/math.gcd(n,m))
    return answer


'''
math 라이브러리의
최소 공배수 : lcm 근데 이건 3.9부터 사용가능하므로 gcd를 이용해서 구함
최대 공약수 : gcd
'''