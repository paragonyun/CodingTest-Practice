def solution(rows, columns, queries):
    answer = []
	# matrix 생성
    init_num = 1
    mat = []
    for row in range(rows):
        tmp_row = []
        for j in range(init_num, init_num+columns):
            tmp_row.append(j)

        mat.append(tmp_row)
        init_num += columns

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1 # 이거 안 하면 out of index 뜸 why? 문제의 좌표는 1부터 시작하기 때문
        tmp = mat[x1][y1] # (x1, y1)의 좌표를 기준값으로 잡음
        mini = tmp # 기준값을 일단 최솟값으로 설정

        for k in range(x1,x2): # 좌변 이동
            test = mat[k+1][y1] # 다음값 확인
            mat[k][y1] = test   # 다음값으로 바꿈(=옮겨줌)
            mini = min(mini, test) # 그 중 최솟값을 확인

        for k in range(y1,y2): # 상변 이동
            test = mat[x2][k+1] 
            mat[x2][k] = test
            mini = min(mini, test)

        for k in range(x2,x1,-1): # 우변 이동 (얘는 내려가야해서 간격을 -1로 해야됨)
            test = mat[k-1][y2]
            mat[k][y2] = test
            mini = min(mini, test)

        for k in range(y2,y1,-1): # 하변 이동
            test = mat[x1][k-1]
            mat[x1][k] = test
            mini = min(mini, test)

        mat[x1][y1+1] = tmp    # 중요!!!! 마지막에 원래 맨 처음이었던 값을 오른쪽으로 돌려줘야됨(x1, y1이니까 무조건 왼쪽 위 꼭지점에 있음 -> 오른쪽으로 한칸 이동해야됨)
        answer.append(mini) # 각 query당 최솟값을 asnwer에 append

    return answer