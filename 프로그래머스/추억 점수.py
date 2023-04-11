def solution(name, yearning, photo):
    answer = []
    for p in photo:
        fin = 0
        for now, score in zip(name, yearning):
            if now in p:
                fin += score
        answer.append(fin)
        
    return answer