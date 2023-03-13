import sys
import heapq

input = sys.stdin.readline
n = int(input())
lecture = []
for i in range(n):
    lecture.append(list(map(int, input().split())))

lecture.sort(key=lambda x :(x[0]))
rooms = [0] #강의 끝나는 시간을 저장하는 heap (최소 힙)
cnt = 1
for start, end in lecture:
    if start >= rooms[0]:
        heapq.heappop(rooms) 
    else:
        cnt += 1
    heapq.heappush(rooms, end) #rooms 힙에 end시간 추가
print(cnt)

