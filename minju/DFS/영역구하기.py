import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split()) #0,2,4,4
    for y in range(y1,y2):
        for x in range(n-x2,n-x1):
            arr[y][x] = 1

def dfs(x, y):
    global cnt
    if x <= -1 or x >= m or y <= -1 or y >= n :
        return False 
    if arr[x][y] == 0 :
        arr[x][y] = 1
        cnt+=1 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return cnt
    return False

result = 0
c =[]
cnt = 0
for i in range(m):
    for j in range(n):
        kk = dfs(i,j)
        if kk != False:
            c.append(kk)
            cnt = 0
            result += 1
                        
c.sort()
print(result)
print(*c)
