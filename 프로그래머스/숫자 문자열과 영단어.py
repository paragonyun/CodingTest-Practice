def solution(s):
    answer = 0
    
    num_lst = ['zero', 'one', 'two', 'three', 'four', 'five', 
                'six', 'seven', 'eight', 'nine']
    
    for i in num_lst :
        s = s.replace(i, str(num_lst.index(i)))
                
    return int(s)