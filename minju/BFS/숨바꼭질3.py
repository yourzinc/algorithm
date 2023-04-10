from collections import deque

n, k = map(int, input().split())

result = [0]*100001
result[n] = 1

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        
        if x == k:
            return result[x]-1
        
        for nx in (x*2, x-1, x+1):
            if 0 <= nx < 100001 and result[nx] == 0:
                if nx == x*2 :
                    result[nx] = result[x]
                    queue.appendleft(nx)
                
                else:
                    result[nx] = result[x] + 1
                    queue.append(nx)             
print(bfs(n))
