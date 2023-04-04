import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, k = map(int,input().split())

arr = [[0]*m for _ in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
    
def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False 
    if arr[x][y] == 1 :
        arr[x][y] = 0
        cnt+=1 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return cnt
    return False  

c =[]
cnt = 0
for i in range(n):
    for j in range(m):
        kk = dfs(i,j)
        if kk != False:
            c.append(kk)
            cnt = 0
                        
print(max(c))
