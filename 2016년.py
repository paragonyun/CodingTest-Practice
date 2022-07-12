def solution(a, b):
    answer = ''
    
    day_31 = [1,3,5,7,8,10,12]
    day_29 = [2]
    day_30 = [4,6,9,11]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    ## 1월이면 그냥 바로 계산해버리면 됨
    if a == 1:
        answer = day[(b % 7) -1] ## 7로 나눠서 0이면 금요일 1이면 토요일이 뜨는 방식
                                ## 1월 1일부터 시작이므로 -1을 해줘야됨
        
    else :
        
        days = 0
        
        ## 1월부터 a-1월까지 돌면서
        for i in range(1, a) :
            if i in day_31 :
                days += 31
            elif i in day_30 :
                days += 30
            elif i == 2 :
                days += 29 ## 2016년은 2월이 29일까지 있었다.
                 
                
        answer = day[(days+b) % 7 -1 ] ## days = 지금까지 경과한 일자
                                    ## +b = 이번달에 지난 날
    

    return answer