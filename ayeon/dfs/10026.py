# [BOJ] 적록색약

# 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역
# 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수

# 적록색약이 아닌 사람이 봤을 때, R, G, B 로 나뉜 구역의 수
# 상하좌우로 dfs 돌면서 방문 처리 후 count

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())
p = [ list(map(str, input())) for _ in range(N) ] # R, B, G
v1 = [ [False]*N for _ in range(N) ] # 방문
v2 = [ [False]*N for _ in range(N) ] # 방문

d = [ (-1,0), (1,0), (0,-1), (0,1) ]

def dfs(i,j,c,v):
    # (i, j) 방문, c는 color list, v는 방문 확인
    v[i][j] = True

    # 인접 (상하좌우)
    for di, dj in d:
        ni = i + di 
        nj = j + dj

        if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
            continue
        
        if not v[ni][nj] and p[ni][nj] in c: # 색깔이 같으고 방문하지 않았다면
            dfs(ni, nj, c, v) # 방문
    
answer1 = answer2 = 0

for i in range(N):
    for j in range(N):
        if not v1[i][j]: # 적록색약 X
            dfs(i, j, [p[i][j]], v1) # 방문
            answer1 += 1

        if not v2[i][j]: # 적록색약 O
            if p[i][j] == 'R' or p[i][j] == 'G':
                dfs(i, j, ['R','G'], v2) # 방문
            else:
                dfs(i, j, ['B'], v2) # 방문
            answer2 += 1

print(answer1, answer2)