def solution(s, skip, index):
    answer = ''
    """
    1. 문자열s의 알파벳을 index만큼 뒤에 알파벳으로 바꿈
    2. z를 넘어가면 a로
    3. skip은 넘어감
    """
    
    alphas = "abcdefghijklmnopqrstuvwxyz"
    
    alphas = [i for i in alphas if i not in skip]
    
    for i in range(len(s)):
        now = alphas.index(s[i]) # 현재 문자가 alphas에 있는 index
        replace_idx = (now + index) % len(alphas) # 대체시킬 문자의 index
        
        answer += alphas[replace_idx]

    return answer