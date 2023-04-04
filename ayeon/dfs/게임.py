# [BOJ] 게임

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(input().rstrip()))
 
visited = [[False]*M for _ in range(N)]
dp = [[0]*M for _ in range(N)]
 
result = 0
def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx = x+int(arr[x][y])*dx[i]
        ny = y+int(arr[x][y])*dy[i]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != "H" and cnt+1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = cnt+1
                visited[nx][ny] = True
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = False
 
dfs(0, 0, 0)
print(result+1)