n = int(input())
score_dict = {"1":[0, 0, []], "2":[0, 0, []]}
winning = ""
for _ in range(n):
    team, goal_time = input().split()
    mm, ss = map(int, goal_time.split(":"))
    score_dict[team][0] += 1
    now_ss = mm * 60 + ss
    if score_dict["1"][0] == score_dict["2"][0]:
        score_dict[winning][1] += now_ss - score_dict[winning][-1][-1]
        winning = ""
    else:
        if winning == team:
            score_dict[winning][1] += now_ss - score_dict[winning][-1][-1]
        if score_dict["1"] > score_dict["2"]: winning = "1"
        else: winning = "2"
    score_dict[team][-1].append(now_ss)

if winning != "":
    score_dict[winning][1] += 48*60 - score_dict[winning][-1][-1]

print(format(score_dict["1"][1]//60, '02') + ":" + format(score_dict["1"][1]%60, '02'))
print(format(score_dict["2"][1]//60, '02') + ":" + format(score_dict["2"][1]%60, '02'))
