import sys 
#input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, list(input()))))

def dfs(x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n :
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
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
for i in range(n):
    for j in range(n):
        kk = dfs(i,j)
        if kk != False:
            c.append(kk)
            cnt = 0
            result += 1
                        
c.sort()
print(len(c))
for i in range(len(c)):
    print(c[i])
