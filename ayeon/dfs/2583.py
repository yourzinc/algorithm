# [BOJ] 영역 구하기

# M, N과 K 그리고 K개의 직사각형의 좌표

# K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지
# 분리된 각 영역의 넓이가 얼마인지 출력

import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
a = [ [0]*N for _ in range(M) ]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            a[y][x] = 1

d = [ (1,0), (-1,0), (0,-1), (0,1) ]

def dfs(i, j, count):
    # i,j 방문
    a[i][j] = 1

    # 상하좌우
    for di, dj in d:
        ni = i + di
        nj = j + dj

        if ni < 0 or ni > M-1 or nj < 0 or nj > N-1:
            continue
        
        if a[ni][nj] == 0: # 비어있으면
            count = max(count, dfs(ni, nj, count+1))
    
    return count

answer = []

for i in range(M):
    for j in range(N):
        if a[i][j] == 0:
            answer.append(dfs(i,j,1))

answer.sort()

print(len(answer))
for a in answer:
    print(a, end =" ")