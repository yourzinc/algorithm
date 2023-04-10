# [BOJ] 영역 구하기

# K 개의 직사각형의 좌표가 주어질 때, K 개의 직사각형 내부를 제외한 나머지 부분이
# 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 출력

# 1. 지도에 위치하는 직사각형에 flag = False 표시
# 2. 지도를 bfs 로 상하좌우로 돌면서 각 영역을 count

from collections import deque

M, N, K = map(int, input().split())

m = [[True]*N for _ in range(M)]


# K개 직사각형
for _ in range(K):
    x0, y0, x1, y1 = map(int, input().split())

    for x in range(x0, x1):
        for y in range(y0, y1):
            m[y][x] = False

d = [ (-1,0), (1,0), (0,-1), (0,1) ]


def bfs(i,j):
    count = 1 # 영역

    q = deque([])
    q.append((i,j))
    m[i][j] = False

    while q:
        qi, qj = q.popleft()

        for di, dj in d:
            ni = qi + di
            nj = qj + dj

            if ni < 0 or ni > M-1 or nj < 0 or nj > N-1 :
                continue
            
            if m[ni][nj] : # 방문하지 않았다면
                m[ni][nj] = False # 방문
                count += 1 # 영역 +1
                q.append((ni,nj))

    return count

answer = []
for i in range(M):
    for j in range(N):
        if m[i][j] :
            answer.append(bfs(i,j))

answer.sort()
print(len(answer))
for a in answer:
    print(a, end=' ')