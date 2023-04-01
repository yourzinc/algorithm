# [BOJ] 경로 찾기

# 가중치 없는 방향 그래프 G
# 모든 정점 (i, j)에 대해서, i에서 j로

N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N) ]

arr2 = [ [0]*N for _ in range(N) ]

def dfs(i,j):
    # i->j 방문
    arr2[i][j] = 1


    # 인접 노드 j->k
    # 방문되지 않았다면
    for k in range(N):
        if arr[j][k] == 1 and arr2[i][k] == 0:
            dfs(i,k) # i->k 방문

if __name__ == "__main__":
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and arr2[i][j] == 0: # i->j 간선이 존재, 방문하지 않았다면
                dfs(i,j) # i->j 방문
    
    for i in arr2:
        for j in i:
            print(j, end=' ')
        print()