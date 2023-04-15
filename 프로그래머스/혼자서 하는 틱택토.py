# def solution(board):
#     answer = -1
    
#     """
#     1. X-O 순서 맞는지 체크
#     2. 게임종료 후 계속하는지 체크
    
#     일단 시작은 무조건 O
#     그다음 x
#     -> 만약 X가 0보다 많으면 그건 규칙을 안 지킴 (순서)
#     -> 만약 ooo, xxx, 대각선 뭐 이런 상황이 2개 이상 발견되면 규칙을 안 지킴
#         -> 가로: 어떻게 체크? 일단 board를 돌면서 cnt += 1 if XXX(OOO) in board: 로 체크 (row로 도니까 금방 확인 가능)
        
#         -> 대각선: 어차피 수가 얼마 안 되니 그냥 체크 
#             -> cross_check = []
#             -> cross_check[0] = board[0][0] + board[1][1] + board[2][2]
#             -> cross_check[1] = board[0][2] + board[1][1] + board[2][0]
#             if "XXX" or "OOO" in cross_check:
#                 cnt += 1
            
#         -> 세로: 
#                 col_check = []
#                 for col in range(3):
#                     tmp_col = ""
#                     for row in range(3): # 콜보다 row를 먼저 보게
#                         tmp_col += board[row][col]
#                     col_check.append(tmp_col)
                
#                 if "XXX" or OOO in col_check:
#                     cnt += 1 # 사실 이거도 갯수마다 더해야함
        
#         -> 이 cnt가 2 이상이면 0return 
        
#     개수 먼저 파악
#     O가 승자일 때 X가 O와 수가 같으면 실패
#     X가 승자일 때 O가 X보다 많으면 실패
#     """

#     # X가 0보다 많은지 체크 
#     X_cnt = 0
#     O_cnt = 0
    
#     # col check
#     col_check = []
    
#     total_cnt = 0
    
#     row_check = []
#     for i in range(3):
#         row_check.append(board[i]) # 가로 방향으로 있나 체크
        
#         tmp_col = "" # 세로방향 체크에 사용될 임시 변수
        
#         for j in range(3):             # X와 O가 각각 몇개있나 체크
#             if board[i][j] == "X":
#                 X_cnt += 1
#             elif board[i][j] == "O":
#                 O_cnt += 1
                
#             # 세로방향 체크를 위해 i를 col로 생각하고 j를 row로 둠
#             tmp_col += board[j][i]
#         # tmp_col 완성이 끝나면 결과를 col_check에 저장
#         col_check.append(tmp_col)
        
#     cross_check = []
#     cross_check.append(board[0][0] + board[1][1] + board[2][2])
#     cross_check.append(board[0][2] + board[1][1] + board[2][0])
    
#     fin_check = []
#     for row in row_check:
#         if row == "XXX" or row == "OOO":
#             total_cnt += 1
#             fin_check.append(row)
#     for cross in cross_check:
#         if cross == "XXX" or cross == "OOO":
#             total_cnt += 1
#             fin_check.append(cross)
#     for col in col_check:
#         if col == "XXX" or col == "OOO":
#             total_cnt += 1
#             fin_check.append(col)
    
#     print("row: ", row_check)
#     print("col: ", col_check)
#     print("cross: ", cross_check)
            
#     if total_cnt >= 2:
#         print("total_cnt가 2 이상임: ", total_cnt)
#         if total_cnt == 2 and fin_check.count("OOO") ==2:              
#             return 1

#         return 0
    
#     if X_cnt > O_cnt:
#         print("X가 더 많음: ", X_cnt, O_cnt)
#         return 0
#     if abs(X_cnt - O_cnt) >= 2:
#         return 0
    
#     if fin_check:
#         if fin_check[0] == "OOO" and X_cnt == O_cnt:
#             return 0
#         elif fin_check[0] == "XXX" and X_cnt < O_cnt:
#             return 0
    
#     return 1

def isWin(board, x, y):
    leftY, rightY = (y - 1) % 3, (y + 1) % 3
    if board[x][y] == board[x][leftY] == board[x][rightY]:
        return True

    upX, downX = (x - 1) % 3, (x + 1) % 3
    if board[x][y] == board[upX][y] == board[downX][y]:
        return True

    if (board[x][y] == board[upX][leftY] == board[downX][rightY]) or (board[x][y] == board[upX][rightY] == board[downX][leftY]):
        return True

    return False

def solution(board):
    n = len(board)

    oList, xList = [], []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'O':
                oList.append((x, y))
            elif board[x][y] == 'X':
                xList.append((x, y))

    if len(oList) < len(xList) or len(oList) >= (len(xList) + 2):
        return 0

    for x, y in oList:
        if isWin(board, x, y) and len(xList) != (len(oList) - 1):
            return 0

    for x, y in xList:
        if isWin(board, x, y) and len(xList) != len(oList):
            return 0

    return 1