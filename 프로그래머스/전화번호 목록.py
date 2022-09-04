'''
이러면 당연하게도 시간초과가 뜬다..
'''

# def solution(phone_book):
    
#     for i in phone_book :
#         new_lst = phone_book.copy()
#         new_lst.remove(i) 
        
#         for j in new_lst :
#             if i in j[:len(i)] :
#                 return False

#     return True
# from collections import deque

# def solution(phone_book):
#     phone_book.sort(key = lambda x: len(x))
#     qu = deque(phone_book)
    
#     while qu :
#         now = qu.popleft()
        
#         for i in qu :
#             if now in i[:len(now)] :
#                 return False
#             ## 어차피 같은 길이의 애들은 한번 지나갔을 때 없으면 안 됨
#             ## 더 긴 애들은 원래 안 됐고
#             ## 때문에 popleft한 거 그냥 다시 안 넣고 놔둠
        
#     return True

def solution(phone_book) :
    
    phone_book.sort()
    
    for i in range(len(phone_book)-1) :
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])] :
            
            return False


    return True

'''
어이가 없네... ㅠㅠㅠㅠ
'''