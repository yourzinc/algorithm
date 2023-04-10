from collections import deque

n, k = map(int, input().split())

result = [0]*100001
cnt = 0

def bfs(x):
    queue = deque()
    queue.append(x)
    global cnt
    while queue:
        x = queue.popleft()
        
        if x == k:
            cnt+=1
        
        for nx in (x-1, x+1, x*2):
            if nx < 0 or nx>= 100001:
                continue
            if result[nx] == 0 or result[nx] == result[x]+1:
                result[nx] = result[x] + 1
                queue.append(nx)

if n == k:
    print(0)
    print(1)
else:
    bfs(n) 
    print(result[k])
    print(cnt)
