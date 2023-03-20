import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
r, c, d = map(int, input().strip().split())
arr = []
global answer
answer = 0

for _ in range(n):
    arr.append(list(map(int, input().strip().split())))

def dfs(r, c, d):
    global answer

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 1. 청소 안 되어있을 경우, 청소함
    if arr[r][c] == 0:
        answer += 1
        arr[r][c] = -1

    # 2. 주변 4칸 중 안 청소된 칸 있는 경우
    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                dfs(nx, ny, d)
                break
    # 3. 주변 4칸이 모두 청소된 경우
    else:
        nx, ny = r - dx[d], c - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                return answer
            else:
                dfs(nx, ny, d)

    return answer

print(dfs(r, c, d))