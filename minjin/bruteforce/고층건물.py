import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
heights = list(map(int, input().strip().split()))

def calc_visibles(now):
    cnt = 0

    # 1. 나보다 앞에 있는 건물들 체크
    max_slope = -1 * INF
    for checking in range(now-1, -1, -1):
        slope = (heights[checking] - heights[now])/abs(checking-now)
        if slope > max_slope:
            max_slope = slope
            cnt += 1

    # 2. 나보다 뒤에 있는 건물들 체크
    max_slope = -1 * INF
    for checking in range(now+1, n):
        slope = (heights[checking] - heights[now]) / abs(checking - now)
        if slope > max_slope:
            max_slope = slope
            cnt += 1

    return cnt

max_cnt = 0
for i in range(n):
    max_cnt = max(max_cnt, calc_visibles(i))

print(max_cnt)