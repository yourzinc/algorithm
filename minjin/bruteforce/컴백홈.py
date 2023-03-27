import sys
input = sys.stdin.readline

r, c, k = map(int, input().strip().split())
graph = []
for _ in range(r):
    graph.append(list(input().strip()))

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[False for _ in range(c)] for _ in range(r)]
def dfs(x, y, depth):
    global answer
    if depth == k and x == 0 and y == c-1:
        answer += 1
        return
    elif depth >= k:
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "T":
            graph[nx][ny] = "T"
            dfs(nx, ny, depth+1)
            graph[nx][ny] = "."

graph[r-1][0] = "T"
dfs(r-1, 0, 1)
print(answer)