# [BOJ] 꽃길

def check(i, j, visited):
    for di, dj in d:
        ni = i + di
        nj = j + dj
        if (ni, nj)  in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer: return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                if check(i, j, visited) and (i, j) not in visited:
                    temp = [(i, j)]
                    temp_cost = fields[i][j]
                    for di, dj in d:
                        ni = i + di
                        nj = j + dj
                        temp.append((ni, nj))
                        temp_cost += fields[ni][nj]
                    dfs(visited + temp, total + temp_cost)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer = int(1e9)
fields = [list(map(int, input().split())) for _ in range(N)]
dfs([], 0)

print(answer)