def make_day(date):
    year, month, day = map(int, date.split("."))
    return year*365 + month*28 + day


def solution(today, terms, privacies):
    answer = []
    
    today_day = make_day(today)

    for term in terms:
        term_category, validation = term.split()

        for idx, privacy in enumerate(privacies):
            start_day, cat = privacy.split()
            
            if cat == term_category:
                year_gap = abs(int(today.split(".")[0]) - int(start_day.split(".")[0]))
                if year_gap > 0:
                    exp_date = make_day(start_day) + 28*(int(validation)+year_gap) +year_gap # 연도 넘어가면 +1 안넘어가면 그대로

                else:
                    exp_date = make_day(start_day) + 28*(int(validation))
                
                if exp_date <= today_day:
                    answer.append(idx+1)

    return sorted(answer)

"""
1. datetime 쓰자니 모든 달이 28일로 고정되어 있어서 그냥 day로 단위를 고정시킴
2. 그 뒤론 문제에 나와있는 거 그대로 씀

계속 테케에서 막혀서 고민했음 -> 생각해보니, year가 n년 차이나는 경우, 그 수치를 계속해서 보정시켜줘야됨 그래서 해줌

if year_gap > 0:
        exp_date = make_day(start_day) + 28*(int(validation)+year_gap) +year_gap 
"""