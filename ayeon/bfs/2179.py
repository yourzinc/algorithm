# [BOJ] 미로탐색

# 1 : 이동할 수 있는 칸
# 0 : 이동할 수 없는 칸

# (1,1) -> (N,M) 위치 이동
# 인접한 칸 : 상하좌우

# 입력 = 미로
# 출력 = 지나야 하는 최소한의 칸 수

# 1. (i,j) 탐색
# 2. 상하좌우 중 이동할 수 있는 칸 -> +1 q 에 넣기

from collections import deque 

d = [ (-1,0), (1,0), (0,-1), (0,1) ]

def bfs():
    q = deque([])

    q.append((0,0))

    while q:
        i, j = q.popleft()
        
        for di, dj in d:
            ni = i + di
            nj = j + dj

            if ni < 0 or ni > N-1 or nj < 0 or nj > M-1:
                continue
            
            if m[ni][nj] == 1: # 이동할 수 있는 칸, 처음 지나는 칸
                m[ni][nj] = m[i][j] + 1 # update
                q.append((ni, nj))


N, M = map(int, input().split())
m = [ list(map(int, input())) for _ in range(N) ]
v = [ [False]*M for _ in range(N) ] 
bfs()
print(m[N-1][M-1])