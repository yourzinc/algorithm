import sys
import heapq

input = sys.stdin.readline
min_heap = []
answer = 0

n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(min_heap, (end, start))

last_fin = 0
for _ in range(len(min_heap)):
    end, start = heapq.heappop(min_heap)
    if start >= last_fin:
        last_fin = end
        answer += 1

print(answer)