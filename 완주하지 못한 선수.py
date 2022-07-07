# 이렇게 하면 효율성 테스트에서 빠꾸먹음 dict 로 접근함
# def solution(participant, completion):
    
#     for i in completion :
#         participant.remove(i)
    
#     return participant[0] 


def solution(participant, completion) :
    dic = {}
    answer = ''
    for i in participant : ## participant 별로 0 생성
        dic[i] = 0 
    
    for j in participant : ## 이름 있으면 +1 
        dic[j] += 1
    
    for x in completion : ## completion에 있으면 -1
        dic[x] -= 1
      
    for key, val in dic.items() : ## 정상적으로 완주한 사람이면 0이어야 하니까 아니면 key값 return
        if val != 0 :
            print(key, val)
            answer = key
    return answer