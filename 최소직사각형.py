def solution(sizes):
    answer = 0
    
    ws = []
    hs = []
    
    for w, h in sizes :
        if w >= h :
            ws.append(w)
            hs.append(h)  
            
        elif w < h :
            ws.append(h)
            hs.append(w)
    
    return max(ws) * max(hs)

'''
둘 중에 큰 걸 가로에 모아두고
작은 건 세롱 모아둔 다음
각 list의 최댓값만 곱해줌
'''