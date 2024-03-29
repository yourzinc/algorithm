# https://www.acmicpc.net/problem/1931
# 회의실 배정

n = int(input())
room = []

for i in range(n):
    a, b = map(int, input().split())
    room.append([a, b])

room.sort(key = lambda x: x[0]) # 시작시간 기준 정렬
room.sort(key = lambda x: x[1]) # 종료시간 기준 정렬

cnt = 1
end = room[0][1]
for i in range(1, n):
    if room[i][0] >= end:
        cnt += 1
        end = room[i][1]

print(cnt)