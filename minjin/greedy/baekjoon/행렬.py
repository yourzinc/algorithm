import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
a_arr = [list(map(int, input().strip())) for _ in range(n)]
b_arr = [list(map(int, input().strip())) for _ in range(n)]

def flip(x, y, arr):
    for a in range(3):
        for b in range(3):
            a_arr[x + a][y + b] = (a_arr[x + a][y + b] + 1) % 2

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if a_arr[i][j] != b_arr[i][j]:
            flip(i, j, a_arr)
            cnt += 1

if a_arr == b_arr:
    print(cnt)
else:
    print(-1)