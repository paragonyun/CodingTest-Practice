
"""처음엔 words[:1]을 [0]으로 풀었었는데 테케에서 실패가 떴다. 처음 숫자가 3인 경우를 고려 안 해서 난 에러인듯하다"""    
    
def solution(s):
    words = s.split(" ")
    
    for i in range(len(words)):
        words[i] = words[i][:1].upper() + words[i][1:].lower()

    return " ".join(words)
