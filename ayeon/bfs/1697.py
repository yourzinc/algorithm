# [BOJ] 숨바꼭질
# 수빈 : N 
# 동생 : K

# 수빈이는 1초 후 -1, +1, *2 의 이동을 할 수 있다

# 동생을 찾을 수 있는 가장 빠른 시간

# SOLUTION 1) memory 초과
# 1. q 에서 popleft() = x(위치) t(시간)
# 2. q.append() :  x-1, x+1, x*2 , t+1 

# SOLUTION 2)
# 1.  -> m 방문처리

from collections import deque

def bfs(N, K):
    q = deque([])
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            return m[K]

        for nx in [x+1, x-1, x*2]:

            if nx < 0 or nx > 100000:
                continue

            if m[nx] == 0:
                m[nx] = m[x] + 1 
                q.append(nx)

N, K = map(int, input().split())

m = [0]*100001

print(bfs(N, K))