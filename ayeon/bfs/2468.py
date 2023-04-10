# [BOJ] 안전 영역

# 물에 잠기는 지점을 표시
# bfs 로 상하좌우 방문

from collections import deque

N = int(input()) # 2~100
m = [ list(map(int, input().split())) for _ in range(N) ]

d = [ (-1,0), (1,0), (0,-1), (0,1) ]

def bfs(i,j,h,v):
    q = deque([])
    q.append((i,j))
    v[i][j] = True # 방문

    while q:
        qi, qj = q.popleft()

        for di, dj in d:
            ni = qi + di
            nj = qj + dj

            if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
                continue
            
            if not v[ni][nj] and m[ni][nj] > h: # 방문하지 않은, 잠기지 않는 지역
                q.append((ni,nj))
                v[ni][nj] = True # 방문



max_h = max(max(m)) # 최대 높이

max_count = 0

for h in range(max_h+1): # 높이가 h 이하
    count = 0

    v = [ [False]*N for _ in range(N) ] # 방문 표시

    for i in range(N):
        for j in range(N):

            if not v[i][j] and m[i][j] > h:
                bfs(i,j,h,v)
                count += 1

    max_count = max(max_count, count)

print(max_count)