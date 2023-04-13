# def solution(cards1, cards2, goal):
#     """인덱스의 순서가 다르면 불가능"""
#     """아래의 코드는 테케에서 에러"""
#     cards1_lst = []
#     cards2_lst = []
    
#     for i in goal:
#         if i in cards1:
#             cards1_lst.append(i)
#         else:
#             cards2_lst.append(i)
    
#     if cards1 == cards1_lst and cards2 == cards2_lst:
#         return "Yes"

#     else:
#         return "No"

def solution(cards1, cards2, goal):
    """이렇게 하면 하나하나 비교를 하니까 모든 경우에 대해 비교 가능"""
    for i in goal:
        if cards1 and cards1[0] == i:
            cards1.pop(0)
        elif cards2 and cards2[0] == i:
            cards2.pop(0)
        else:
            return "No"
    
    return "Yes"
    