# [BOJ] 1987 알파벳
# 4/2 10:46 - 11:12

# 세로 R칸, 가로 C칸
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동
# 같은 알파벳이 적힌 칸을 두 번 지날 수 없다

# 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램


# dfs : 방문 처리 = v 라는 배열에 + [] 배열 요소를 추가

import sys
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())

m = [ list(map(str, input())) for _ in range(R) ]

d = [ (-1,0), (1,0), (0,-1), (0,1) ]

def dfs(i, j, v, alphabet): # (i,j) 방문
    
    # 인접 노드
    for di, dj in d:
        ni = i + di
        nj = j + dj

        if ni > R-1 or ni < 0 or nj > C-1 or nj < 0 :
            continue
        
        if (ni,nj) not in v and m[ni][nj] not in alphabet:
            # 방문
            dfs(ni, nj, v + [(ni, nj)], alphabet + [m[ni][nj]])

    
    global answer
    answer = max(answer, len(alphabet))

global answer
answer = 1
dfs(0,0,[(0,0)],[m[0][0]])

print(answer)