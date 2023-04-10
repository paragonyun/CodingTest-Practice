## 시간초과
# def solution(players, callings):
#     answer = []
    
#     for call in callings:
#         now_idx = players.index(call)
#         player = players.pop(now_idx)
#         go_back = players.pop(now_idx-1)
#         players.insert(now_idx-1, player) 
#         players.insert(now_idx, go_back)
        
#     return players
# from collections import Counter
# def solution(players, callings):
#     ranks = {player:idx  for idx, player in enumerate(players)}
#     cnts = Counter(callings)
#     for player in cnts:
#         now = ranks[player] - cnts[player]
#         for k in ranks:
#             if ranks[k] == now:
#                 ranks[k] += cnts[player]

#         ranks[player] -= cnts[player] # 불린 인원에 대해 순위 조정
        
#     answer = [k for k,_ in sorted(ranks.items(), key=lambda x: x[1])]
    
#     return answer
## 결국 ... 
def solution(players, callings):
    rankDic = {}
    playerDic = {}

    for idx, player in enumerate(players):
        rankDic[idx + 1] = player # 순위: 이름
        playerDic[player] = idx + 1 # 이름: 순위

    for cur_player in callings:
        cur_rank = playerDic[cur_player] # 현재 불린 사람의 순위
        prev_rank = cur_rank - 1         # 순위 하나 빼줌
        prev_player = rankDic[prev_rank] # 역전 당한 사람 확인

        rankDic[cur_rank - 1], rankDic[cur_rank] = rankDic[cur_rank], rankDic[cur_rank - 1]  # 서로 value값을 바꿔줌... 하... 이걸 왜 못 떠올렸을까...
        playerDic[prev_player], playerDic[cur_player] = playerDic[cur_player], playerDic[prev_player] # 서로 value값을 바꿔줌

    return list(rankDic.values())