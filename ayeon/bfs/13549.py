# [BOJ] 숨바꼭질 3 (-)

# 1초 후 x-1, x+1 로 이동
# 0초 후 2*x 로 이동

from collections import deque

def bfs(N,K):
    q = deque([])
    q.append(N)
    m[N] = 0 # 방문

    while q:
        x = q.popleft() # 현재 위치
        if x == K:
            return

        # 0초
        nx = x*2
        if nx <= 1e6 and m[nx] == -1: # 방문하지 않았다면
            m[nx] = m[x]
            q.append(nx)

        # 1초
        for nx in [x+1, x-1]:
            if nx > -1 and nx <= 1e6 and m[nx] == -1: # 방문하지 않았다면
                m[nx] = m[x] +1
                q.append(nx)


N, K = map(int, input().split())

m = [-1]*100001
bfs(N,K)

print(m[K])