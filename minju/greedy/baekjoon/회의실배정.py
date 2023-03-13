import sys
input = sys.stdin.readline
n = int(input())
meeting = []
for i in range(n):
    start, end = map(int, input().split())
    meeting.append([start ,end])
    
meeting.sort(key=lambda x: (x[1],x[0]))
sum = 0
cnt = 0
for i in range(len(meeting)):
  if meeting[i][0] >= sum:
    sum = meeting[i][1]
    cnt += 1
  else:
    continue
print(cnt)
