from collections import defaultdict
def solution(survey, choices):
    answer = 'RCJA'
    counter = 'TFMN'
    new = ''
    
    dic = defaultdict(int)
    
    for pair, score in zip(survey, choices) :
        adding = abs(4-score)
        if score <= 3 :
            dic[pair[0]] += adding
        elif score >= 5 :
            dic[pair[1]] += adding
        else :
            continue

    for l, r in zip(answer, counter) :
        if dic[l] < dic[r] :
            new += r 
        else :
            new += l

    return new