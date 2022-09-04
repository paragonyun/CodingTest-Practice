ext = "~!@#$%^&*()=+[{]}:?,<>/"

def solution(new_id):
    
    # 1 단계
    new_id = new_id.lower()
    
    # 2 단계
    for i in ext :
        new_id = new_id.replace(i, '')
    
    # 3 단계
    # 이렇게 축약한 뒤에도 .. 이 남아있는 경우가 있어서 반복분 사용
    # new_id = new_id.replace('..','.') 
    while '..' in new_id : 
        new_id = new_id.replace('..','.')
    
    # 4 단계
    new_id = new_id.strip('.')
        
    # 5 단계
    if len(new_id) == 0 :
        new_id ='a'
        
    # 6 단계
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')



    # 7 단계
    if len(new_id) <= 2 :
        while len(new_id) < 3 :
            new_id += new_id[-1]
        
    
    return new_id