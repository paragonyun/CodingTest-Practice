def solution(d, budget):
    answer = 0
    for i in sorted(d) : 
        if budget - i >=0 :
            answer += 1
            budget -= i
        else : 
            break
    return answer

'''
sort 후 차례대로 빼주면 어차피 최대로 줄 수 있는 경우를 구할 수 있다!
'''