import sys 
from collections import deque
input = sys.stdin.readline
#sys.setrecursionlimit(10**9)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]    
    
def bfs(x,y,h):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx>=n or ny <0 or ny>=n:
                continue
            if visited[nx][ny] ==0 and arr[nx][ny] > h:
                visited[nx][ny] = 1
                queue.append((nx,ny))

result = []
for h in range(max(max(arr))):
    cnt = 0
    visited = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and visited[i][j] == 0:
                bfs(i,j,h)
                cnt+=1
    result.append(cnt)
print(max(result))
