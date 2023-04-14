def converter(string):
    """ string타입 시간을 분단위의 int값으로 반환하는 함수"""
    h,m = string.split(":")
    return int(h)*60+int(m)

def solution(book_time):
    """생각
    1. 일단 start 시간 기준 sorting
    2. dictionary를 돌면서 모든 방의 마지막 퇴실 시간과 비교. 
    3. 퇴실시간 + 10 >= 입실시간 -> 방 하나 더 필요
    3-1. 
    4. 퇴실시간 + 10 < 입실시간 -> 그 방 dictionary에 값 삽입
    5. return len of dictionary
    """
    sorted_book_time = sorted(book_time, key=lambda x: (x[0], x[1]))
    dic = {}
    no_room = 0
    for now_time in sorted_book_time:
        if len(dic) == 0:
            dic[0] = [now_time[1]]
            continue
        
        for room, booked_times in dic.items(): # 처음부터 쭉 돌면서 확인
            pre_out_time = converter(booked_times[-1])
            convted_now_time = converter(now_time[0])

            if pre_out_time + 10 > convted_now_time: # 처음부터 돌면서 보는데, 막혀있음 -> 다음방으로 넘어감 근데 다음 방도 체크해봐야됨.
                # 만약 현재 room == len(dic)-1 이면 끝까지 다 확인해봤다는 소리 -> 이땐 만들어야됨
                if room == len(dic)-1:
                    no_room += 1 #다음 방 지정
                    dic[no_room] = [now_time[1]]
                    break
                    
                # 위와 같은 상황 아니면 그냥 다음 방 체크
                continue
                
            elif pre_out_time + 10 <= convted_now_time: # 넣을 수 있으면 append로 room에 넣음
                dic[room].append(now_time[1])
                break

    return len(dic)