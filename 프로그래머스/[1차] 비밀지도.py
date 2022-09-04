def convert(n, base) :
    converted = ''
    
    while n : ## n이 양수면 계속 돌아감
        n, mod = divmod(n, base) 
        converted = str(mod) + converted
        
    return converted   


def solution(n, arr1, arr2):
    map1 = [convert(i, 2) for i in arr1]
    for idx, i in enumerate(map1) :
        if len(i) != n :
            map1[idx] = '0'*(n-len(i))+i
            
        else :
            continue
    
    map2 = [convert(i, 2) for i in arr2]
    
    for idx, i in enumerate(map2) :
        if len(i) != n :
            map2[idx] = '0'*(n-len(i)) + i
            
        else :
            continue

    result = []
    for ar1, ar2 in zip(map1, map2) :
        for a, b in zip(ar1, ar2) :
            result.append(int(a) + int(b))
    

    fin = ''
    answer = []
    
    for idx, i in enumerate(result) :

        
        if i == 1 or i == 2 :
            fin += '#'
        
        elif i == 0 :
            fin += ' '
                    
        if len(fin) == n :
            answer.append(fin)
            fin = ''
            
    return answer