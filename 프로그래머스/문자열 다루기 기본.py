def solution(s):
    lst = ['0','1','2','3','4','5'
          , '6', '7', '8', '9']
    if ( len(s) == 4 or len(s) == 6 ) :
        for i in s :
            if i not in lst :
                return False
        else : 
            return True
        
    return False

    '''
    def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

    python의 isdigit이라는 함수가 있음. 이거 잘 활용해보셈!!1

    언제 한번 velog에 코테에 유용한 함수 정리할 것
    
    '''