# [BOJ] 음식물 피하기

# 세로 N, 가로 M, 음식물 쓰레기 개수 K

from collections import deque

N, M, K = map(int, input().split())

m = [[0]*M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())    
    m[r-1][c-1] = 1

d = [ (-1,0), (1,0), (0,-1), (0,1) ]

def bfs(i, j):
    # i, j 는 음식물 
    q = deque([])
    q.append((i,j))
    m[i][j] = 0
    count = 1

    while q:
        qi, qj = q.popleft()

        for di, dj in d:
            ni = qi + di
            nj = qj + dj

            if ni < 0 or ni > N-1 or nj < 0 or nj > M-1:
                continue
            
            if m[ni][nj] : # 음식물이면
                count += 1 
                q.append((ni,nj))
                m[ni][nj] = 0 
    
    return count

answer = 0
for i in range(N):
    for j in range(M):
        if m[i][j] == 1:
            answer = max(answer, bfs(i,j))

print(answer)