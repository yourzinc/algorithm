from collections import deque
f, s, g, u, d = map(int, input().split())

result = [0]*(f+1)

def bfs(x):
    queue = deque()
    queue.append(x)
    result[s] = 1
    while queue:
        x = queue.popleft()
        
        if x == g:
            return result[x]-1
        
        for nx in (x-d, x+u):
            if nx <= 0 or nx>= f+1:
                continue
            if result[nx] == 0 :
                result[nx] = result[x] + 1
                queue.append(nx)
    return "use the stairs"

print(bfs(s))     
