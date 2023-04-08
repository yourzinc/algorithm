# [BOJ] 숨바꼭질 2

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
# 가장 빠른 시간으로 찾는 방법이 몇가지

# bfs 로 가장 빠른 시간 찾기

from collections import deque

def bfs(N,K):
    q = deque([])
    q.append(N)

    count = 0

    while q:
        x = q.popleft()
    
        if x == K: # K 위치로 올 수 있는 경우 count 하기
            count += 1
            continue

        for nx in [x+1, x-1, x*2]:
            if nx < 0 or nx > 100000:
                continue

            if m[nx] == m[x] + 1: # 최단 거리로 갈 수 있는 경우 q에 추가
                q.append(nx)

            if m[nx] == 0:
                m[nx] = m[x] + 1
                q.append(nx)

    return count

N, K = map(int, input().split())
m = [0]*100001

count = bfs(N,K)
print(m[K])
print(count)