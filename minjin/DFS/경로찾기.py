import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip().split())))

answer = [[0 for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(n)]

def dfs(x):
    for y in range(n):
        if graph[x][y] == 1 and not visited[y]:
            visited[y] = True
            dfs(y)

def solution():
    global visited
    for i in range(n):
        dfs(i)
        for j in range(n):
            if visited[j]:
                answer[i][j] = 1
        visited = [0 for _ in range(n)]

solution()
for row in answer:
    print(*row)