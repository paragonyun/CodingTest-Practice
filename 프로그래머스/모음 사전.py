from itertools import product
def solution(word):
    """일단 모든 경우의 수를 다 만들고
    sorting?"""
    
    words = ["A", "E", "I", "O", "U"]
    alphas = []
    
    for i in range(len(words)+1):
        possibles = product(words, repeat=i)
        for j in possibles:
            alphas.append("".join(j))
            
    sorted_alphas = sorted(alphas)[1:]
    
    return sorted_alphas.index(word) + 1