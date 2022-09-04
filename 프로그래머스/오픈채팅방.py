def solution(record):
    answer = []
    names = {}
    for sentence in record :
        sentence = sentence.split()
        status, user_id = sentence[0], sentence[1]

        if status == 'Enter' : 
            names[user_id] = sentence[2] ## {user_id : name} 식으로 저장
            
        elif status == 'Change' :
            names[user_id] = sentence[2] ## 이름 바꿔주기
    ## 여기 한번 더 돌아주는 게 좀 보기 싫은데... ##
    for i in record : 
        sentence = i.split()
        status, user_id = sentence[0], sentence[1]
        
        if status == 'Enter' : 
            answer.append(f"{names[user_id]}님이 들어왔습니다.")
            
        elif status == 'Leave' :
            answer.append(f"{names[user_id]}님이 나갔습니다.")
        
    return answer