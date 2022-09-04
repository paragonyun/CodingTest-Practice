def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)) :
        row_sum = []
        for j in range(len(arr1[0])) :
            row_sum.append(arr1[i][j] + arr2[i][j])
            
        answer.append(row_sum)
    
    return answer