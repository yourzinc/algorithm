import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))  
    
def dfs(x,y,h):
    if x<=-1 or x>=n or y<=-1 or y>=n :
        return False
    if visited[x][y] ==0 and arr[x][y] > h:
        visited[x][y] = 1
        dfs(x-1, y,h)
        dfs(x, y-1,h)
        dfs(x+1, y,h)
        dfs(x, y+1,h)
        return True
    return False


result = []
for h in range(101):
    cnt = 0
    visited = [[0] * (n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            check = dfs(i,j,h)
            if check != False:
                cnt+=1
    result.append(cnt)
print(max(result))
