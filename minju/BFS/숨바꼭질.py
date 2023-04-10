from collections import deque

n, k = map(int, input().split())

result = [0]*100001

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        
        if x == k:
            return result[x]
        
        for nx in (x-1, x+1, x*2):
            if nx < 0 or nx>= 100001:
                continue
            if result[nx] == 0 :
                result[nx] = result[x] + 1
                queue.append(nx)
                         
print(bfs(n))            
