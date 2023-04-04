# [BOJ] 음식물 피하기

# 통로의 세로 길이 N, 가로 길이 M
# 음식물 쓰레기 개수 K
# 음식물이 떨어진 좌표 (r,c) : 위로 r만큼, 왼쪽에서 c만큼

# 상하좌우
# 음식물 중 가장 큰 음식물의 크기를 출력

import sys
sys.setrecursionlimit(10**6)

N, M, K  = map(int, input().split())

arr = [ [0]*M for _ in range(N) ]

for _ in range(K):
    r, c = map(int, input().split())

    arr[r-1][c-1] = 1

d = [ (1,0), (-1,0), (0,-1), (0,1) ]

answer = 0

def dfs(i, j, count):
    # i, j 방문
    arr[i][j] = 0
    
    # 상하좌우 확인
    for di, dj in d:
        ni = i+di
        nj = j+dj

        if ni > N-1 or ni < 0 or nj > M-1 or nj < 0 :
            continue

        if arr[ni][nj] == 1:
            count = max(count, dfs(ni, nj, count+1))
        
    return count
        
        
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1: # 음식물이 있으면 dfs
            count = dfs(i, j, 1)
            answer = max(answer, count)
            
print(answer)