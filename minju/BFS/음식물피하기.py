from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())

arr = [[0]*m for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
    
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt
        
c =[]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ans = bfs(i,j)
            c.append(ans)
                        
print(max(c))
