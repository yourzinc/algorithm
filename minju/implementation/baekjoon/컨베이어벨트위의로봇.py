import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
res = 1

while True:
	#1
	belt.rotate(1) #rotate는 오른쪽 회전
	robot.rotate(1)
	robot[-1] = 0 #로봇이 내려가는 부분이니 0
	#2
	if robot: #로봇이 존재하면
		for i in range(n-2, -1, -1): #로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
			if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1: #다음 칸의 로봇이 없고, 내구도가 1이상
				robot[i+1] = 1
				robot[i] = 0
				belt[i+1] -= 1
		robot[-1] = 0 #이 부분도 로봇 out -> 0임
	#3
	if robot[0] == 0 and belt[0]>=1: #올리는 위치에 로봇이 없고,칸의 내구도 0이 아니면
		robot[0] = 1
		belt[0] -= 1
	#4
	if belt.count(0) >= k:
		break

	res += 1

print(res)
