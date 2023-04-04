import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n =int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
    
green_arr = copy.deepcopy(arr)
for i in range(n):
    for j in range(n):
        if green_arr[i][j] == 'G':
            green_arr[i][j] == 'R'

def dfs(arr,x,y,c):
    if x <= -1 or x >=n or y <= -1 or y >= n:
        return False
    if visited[x][y]==0 and arr[x][y] == c :
        visited[x][y] =1
        dfs(arr,x+1,y,c)
        dfs(arr,x-1,y,c)
        dfs(arr,x,y+1,c)
        dfs(arr,x,y-1,c)
        return True
    return False

color = ['R','G','B']
result = []
for c in color:
    cnt = 0
    visited = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            check = dfs(arr,i,j,c)
            if check != False:
                cnt+=1
    result.append(cnt)
    
green_result = []
for c in color:
    cnt = 0
    visited = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            check = dfs(green_arr,i,j,c)
            if check != False:
                cnt+=1
    green_result.append(cnt)    
    
print(sum(result),sum(green_result))
