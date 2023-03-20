import sys
input = sys.stdin.readline

h, w = map(int, input().split())
sky = [list(input().strip()) for _ in range(h)]
answer = [[-1] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if sky[i][j] == "c":
            answer[i][j] = 0
        else:
            if j > 0 and answer[i][j-1] >= 0:
                answer[i][j] = answer[i][j-1] + 1

for row in range(h):
    print(*answer[row])