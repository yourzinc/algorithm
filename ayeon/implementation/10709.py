# 각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름

import sys
input = sys.stdin.readline

H, W = map(int, input().split())

sky = []
for _ in range(H):
    sky.append(list(map(str, input())))

answer = [ [ -1 for _ in range(W)] for _ in range(H) ]

# 처음부터 구름이 떠 있는 경우
for i in range(H):
    for j in range(W):
        if sky[i][j] == 'c':
            answer[i][j] = 0

# 1초씩 확인
time = 1

for i in range(H):
    for j in range(W):
        if answer[i][j] == 0:
            for k in range(1, W-1):
                if j+k < W and answer[i][j+k] < 0:
                    answer[i][j+k] = k
                else:
                    break

for a in answer:
    p = ''
    for b in a:
        p += str(b) + ' '
    p = p[:-1]
    print(p)