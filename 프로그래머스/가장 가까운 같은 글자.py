from collections import defaultdict


def solution(s):

    answer = []
    idx_dict = defaultdict(lambda: -1)

    for idx, i in enumerate(s):

        if idx_dict[i] == -1:  # 처음 등장했으면
            idx_dict[i] = idx
            answer.append(-1)

            continue

        # 처음이 아닌 경우
        now = idx - idx_dict[i]
        idx_dict[i] = idx
        answer.append(now)

    return answer


"""
레벨 1임에도 불구하고 너무 해맸다... 짜증난다 ㅠㅠ
"""
