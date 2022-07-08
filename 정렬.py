def solution(array, commands):
    answer = []
    
    for idx, i in enumerate(commands) :
        arr = sorted(array[commands[idx][0]-1 : commands[idx][1]])
        answer.append(arr[commands[idx][-1]-1])
        
    return answer