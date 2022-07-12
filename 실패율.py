from collections import Counter
def solution(N, stages):
    answer = []
    same = []
    
    dic = Counter(stages) ## 이러면 각 스테이지에 얼마나 머물고 있는지를 확인 가능
    
    ## dic를 stage로 정렬해줌 (실패율을 구하기 위해)
    dic = sorted(dic.items())   
    
    # stage 전체 생성을 위한 dictionary
    sta = {}
    for i in range(1,N+1) :
        sta[i] = 0
        
        
    
    ## 나눠주는 수 처음 값을 위한 정의
    person = len(stages)

    for idx, (stage, num) in enumerate(dic) :
        ## 각 스테이지의 실패율을 구해줌
        sta[stage] = num/person
        ## 거기서 claer한 사람 수는 빼줘서 다시 재정의
        person = (person-num)
        
        ## 마지막 스테이지까지 클리어 했을 때
        if stage == N+1 :
            ## pop으로 클리어한 걸 마지막 스테이지의 실패율로 바꿔줌
            sta[N] == sta.pop(stage)
    
    ## sort diationary by value
    sorted_failure = sorted(sta.items() , key = lambda x : x[1] , reverse=True)
    
    ## i 만 append
    for i,j in sorted_failure :
        answer.append(i)
    
    
    
    return answer

'''
pop으로 old key 이름 바꾸기 방법
dictionary sort 방법 (Value 기준)
'''