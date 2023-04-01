# [BOJ] 단지번호붙이기

# 첫 번째 줄에는 총 단지수를 출력
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

# 1) dfs 로 돌면서 count
# 2) answer 배열에 count 를 추가
# 3) answer 정렬하기

import sys
sys.setrecursionlimit(10**6)

N = int(input())

m = [ list(map(int, input())) for _ in range(N) ]

d = [ (1,0), (-1,0), (0,-1), (0,1) ]

def dfs(i, j, count):
    # i,j 방문
    m[i][j] = 0

    # 상하좌우
    for di, dj in d:
        ni = i + di
        nj = j + dj

        if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:
            continue
        
        if m[ni][nj] == 1: # 방문하지 않은 집이 있다면
            count = max(count, dfs(ni, nj, count+1)) # 방문
    
    return count

answer = []

for i in range(N):
    for j in range(N):
        if m[i][j] == 1: # 집이 있다면
            count = 1
            answer.append(dfs(i, j, count))

answer.sort()

print(len(answer))
for a in answer:
    print(a)