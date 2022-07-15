def solution(s, n):
    answer = ''
    
    lst = "abcdefghijklmnopqrstuvwxyz"
    
    for i in s :
        # 공백은 그냥 추가하고 넣어버림
        if i == ' ' :
            answer += ' '
            continue 
            
        if i.upper() :
            i_ = i.lower()
        
            ## lst.index(i) : lst에 있는 i의 index 반환 
            ## +n : 이동
            ## 알파벳은 25개 -> %26의 나머지로 리스트를 순환시킴
            type_obj = lst[(lst.index(i_)+n)%26]
        
        if i.islower()  :
            print(type_obj)
            answer += type_obj
            
        elif i.upper()  : 
            print(type_obj)
            answer += type_obj.upper()
        
    return answer

'''
list를 순환해야 할 때는 %를 쓰자 (len(list) + 1)
'''