# [BOJ] 스타트와 링크

# N/2 명으로 스타트팀, 링크팀을 나눈다

import sys
input = sys.stdin.readline

from itertools import combinations

# 입력
N = int(input())
v = [ list(map(int, input().split())) for _ in range(N) ]

# 완전탐색
l = list(range(0, N))

result = 100 * 20 * 20

# nCn/2 선택
for c in combinations(l, N//2): # 184756

    # 한 팀의 능력치 합 구하기
    s = 0
    for i in c: # 10 
        for j in c: # 10 
            s += v[i][j]
    
    # 다른 팀 능력치 합 구하기
    d = list(set(l) - set(c))
    t = 0
    for i in d:
        for j in d:
            t += v[i][j]

    result = min(result, abs (t-s))

print(result)