def get_answer(idx, n):
        
    answer = []
    k_th, n_th = (idx // n) + 1, (idx % n) + 1
    if n_th == 0:
        answer.append(n)
    else:
        answer.append(n_th)
    
    if n == 2:
        answer.append(k_th)
    else:
        answer.append(k_th)
    
    return answer
def solution(n, words):

    already = []
    answer = []
    for idx, word in enumerate(words):
        
        if len(already) > 0:
            before = already[-1][-1]
            now = word[0]
            
            if now != before:
                answer = get_answer(idx, n)

                return answer

        if word in already:
            answer = get_answer(idx, n)
            
            return answer
        
        already.append(word)
    
    return [0,0]