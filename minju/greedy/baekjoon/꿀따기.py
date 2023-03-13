import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
target = sum(m[:]) # 전체 꿀의 양
answer = 0
temp = m[0] #중간 벌이 못 먹는 꿀의 양 

# 벌 - 벌 - 꿀인 경우
for i in range(1, n):
    temp += m[i] # 중간 벌이 못 먹는 꿀의 양
    answer = max(answer, target - m[0] - m[i] + target - temp) # 첫 번째 벌이 먹을 수 있는 꿀의 양 + 두번째 벌이 먹을 수 있는 꿀의 양

# 꿀 - 벌 - 벌인 경우
m.reverse() #방향 뒤집기
temp = m[0]
for i in range(1, n):
    temp += m[i] # 중간 벌이 못 먹는 꿀의 양
    answer = max(answer, target - m[0] - m[i] + target - temp) # 첫 번째 벌이 먹을 수 있는 꿀의 양 + 두번째 벌이 먹을 수 있는 꿀의 양


# 벌 - 꿀 - 벌인 경우
for i in range(1, n):
    answer = max(answer, target - m[0] - m[-1] + m[i]) # 모든 곳에 꿀을 한번씩 먹고 꿀통 지점의 꿀을 한번 더 먹는다.


print(answer)
