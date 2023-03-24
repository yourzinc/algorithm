# [BOJ] 컴백홈
# 3/24 9:13 - 9:33

# 한수 : 왼쪽 아래
# 집 : 오른쪽 위

# 지나간 곳은 다시 방문 X


# INPUT
R, C, K = map(int, input().split())
m = [ list(map(str, input())) for _ in range(R) ]

answer = [0]*(R*C)
visited = [ [False for _ in range(C)] for _ in range(R) ]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(i,j,k):
    # i,j 위치
    # k 는 현재 거리
    
    # 만약 현재 위치가 집이라면
    if i == 0 and j == C-1:
        # 도착! 
        # 현재 거리 저장하기
        answer[k] += 1
        return 
    
    # 현재 노드가 가지 못하는 부분이 아니라면
    if m[i][j] != 'T':
        # 현재노드 방문처리
        visited[i][j] = True
        
        # 인접노드 중에서, 방문하지 않은 노드 방문
        for di, dj in move:
            ni = i + di
            nj = j + dj
            
            if ni < 0 or ni >= R or nj < 0 or nj >= C:
                continue
            
            
            if not visited[ni][nj]:
                dfs(ni, nj, k+1)
        
        # 현재노드 방문 Roll back
        visited[i][j] = False

dfs(R-1, 0, 0)
print(answer[K-1])