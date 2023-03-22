import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().strip().split())))

pool = [i for i in range(1, n+1)]
combs = list(map(list, combinations(pool, len(pool)//2)))

def calc_sum(team):
    sum = 0
    for per1 in team:
        for per2 in team:
            sum += data[per1-1][per2-1]
    return sum

def make_another_team(team):
    result = []
    for person in pool:
        if person not in team:
            result.append(person)
    return result


min_gap = int(1e9)
for c in combs:
    team1, team2 = c, make_another_team(c)
    min_gap = min(min_gap, abs(calc_sum(team1) - calc_sum(team2)))

print(min_gap)