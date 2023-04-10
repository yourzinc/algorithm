# [BOJ] 나이트의 이동

from collections import deque

T = int(input()) # 테스트 케이스

d = [(-1,-2), (-2,-1), (-2,1), (-1,2), 
     (1, -2), (2, -1), (2, 1), (1, 2) ]

def solution(l, x0, y0, x1, y1):
    m = [ [0]*l for _ in range(l) ]

    q = deque([])
    q.append((x0,y0))

    if x0 == x1 and y0 == y1:
        return 0

    while q:
        i, j = q.popleft()

        for di, dj in d:
            ni = i + di
            nj = j + dj

            if ni < 0 or ni > l-1 or nj < 0 or nj > l-1:
                continue
            
            if m[ni][nj] == 0: # 방문하지 않았다면
                m[ni][nj] = m[i][j] + 1
                q.append((ni,nj)) 

                if ni == x1 and nj == y1:
                    return m[ni][nj]



while T:
    l = int(input()) # 체스판 한 변의 길이
    x0, y0 = map(int, input().split()) # 현재 있는 칸
    x1, y1 = map(int, input().split()) # 이동하려고 하는 칸

    print(solution(l, x0))

    T -= 1
