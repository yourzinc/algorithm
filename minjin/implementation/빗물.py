import sys
input = sys.stdin.readline

h, w = map(int, input().strip().split())
heights = list(map(int, input().strip().split()))
water = 0
peak = max(heights)

high_point = 0
# 앞에서부터 peak까지
for i in range(heights.index(peak)):
    if heights[i] < high_point:
        water += high_point - heights[i]
    else:
        high_point = heights[i]

high_point = 0
# 뒤에서부터 peak까지
for j in range(len(heights)-1, heights.index(peak), -1):
    if heights[j] < high_point:
        water += high_point - heights[j]
    else:
        high_point = heights[j]

print(water)