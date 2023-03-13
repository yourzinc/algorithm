import sys
import heapq
input = sys.stdin.readline
n = int(input())
meeting = []
for i in range(n):
    meeting.append(list(map(int, input().split())))
    
meeting.sort(key=lambda x :(x[0])) 
rooms = [0] #회의실의 끝나는 시간을 저장하는 heap (최소 힙)
cnt = 1
for start, end in meeting:
    if start >= rooms[0]:
        heapq.heappop(rooms) 
    else:
        cnt += 1
    heapq.heappush(rooms, end) #rooms 힙에 end시간 추가
print(cnt)

좋아요공감
공유하기
