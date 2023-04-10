from collections import deque
import sys

input = sys.stdin.readline
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split()) #0,2,4,4
    for y in range(y1,y2):
        for x in range(n-x2,n-x1):
            arr[y][x] = 1


# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    cnt = 1
    arr[x][y] =1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx>=m or ny <0 or ny>=n:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                cnt+=1
                queue.append((nx,ny))
    return cnt

c =[]
for i in range(m):
    for j in range(n):
        if arr[i][j] ==0:
            ans = bfs(i,j)
            c.append(ans)
                        
c.sort()
print(len(c))
print(*c)
