# [BOJ] 안전 영역

# 1. 물에 잠기는 지점을 arr2에 표시 (h 보다 작으면 true, 아니면 else)
# 2. arr2를 돌면서, dfs 로 인접한 부분이 없을 때까지 탐색

# 틀린 부분
# 1)
# i+di > N-1 or i < 0 or j+dj > N-1 or j < 0:

# 2) 
# h_max = 는 0 의 값부터!

import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    # i, j 방문
    arr2[i][j] = 1

    # 인접 노드 탐색 (상하좌우)
    for di, dj in d:
        if i+di > N-1 or i+di < 0 or j+dj > N-1 or j+dj < 0:
            continue
        if arr2[i+di][j+dj] == 0: # 방문하지 않은 잠기지 않는 지역이면 
            dfs(i+di, j+dj) # 방문

def check(i, j, h):
    if arr[i][j] <= h:
        arr2[i][j] = 1 # 물에 잠기면 1
    else:
        arr2[i][j] = 0 # 아니면 0 


N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N) ]
arr2 = [ [0]*N for _ in range(N) ] # 물에 잠기면 1, 아니면 0, 방문하면 1

d = [ (-1,0), (1,0), (0,-1), (0,1) ]

h_max = max(max(arr))

answer = 0

for h in range(h_max+1): # 높이 = 0, 1, 2, ... h_max

    count = 0 # 안전 영역

    # 물에 잠기는 지점 표시
    for i in range(N):
        for j in range(N):
            check(i, j, h)
    # 탐색
    for i in range(N):
        for j in range(N):
            if arr2[i][j] == 0: 
                dfs(i,j)
                count += 1
    
    # 갱신
    answer = max(answer, count)

print(answer)