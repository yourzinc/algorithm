# [BOJ] 숨바꼭질 4

# 수빈 N
# 동생 K

# 1초 후, -1, +1, *2

# 가장 빠른 시간
# 이동하는 길

# N = K 인 경우

from collections import deque

v = [0]*100001
p = [0]*100001 # 부모 노드 저장

def bfs(N, K):
    q = deque([])
    q.append(N)
    p[N] = -1

    while q:
        x = q.popleft()

        if x == K:
            return v[K]

        for nx in [x-1, x+1, x*2]:
            if nx < 0 or nx > 100000:
                continue

            if not v[nx]:
                v[nx] = v[x] + 1
                q.append(nx)
                if not p[nx]:
                    p[nx] = x


def path(K):
    s = []
    s.append(K)

    i = p[K] # 자식 -> 부모

    while i >= 0:
        s.append(i)
        i = p[i]
    
    for i in s[::-1]:
        print(i, end=' ')


N, K = map(int, input().split())
print(bfs(N,K))
path(K)