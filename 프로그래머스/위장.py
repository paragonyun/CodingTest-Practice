"""각 category별로 상품 수 구한 다음에, 조합으로 경우의수 + category하나씩 할 때 수"""

def solution(clothes):
    answer = 0
    
    dic = {cat:[] for item, cat in clothes}
    
    for item, cat in clothes:
        dic[cat].append(item)
    
    fin = 1
    for item in dic.values():
        fin *= (len(item)+1)
    
        
    return fin -1