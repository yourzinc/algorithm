# # 시도 1
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().strip().split())
# arr = list(map(int, input().strip().split()))
# # robots = [False] * (2 * n)
# for i in range(len(arr)):
#     arr[i] = [arr[i], False]
# stage = 0
#
# while True:
#
#     cnt = 0
#     for a in arr:
#         if a[0] == 0:
#             cnt += 1
#     if cnt >= k:
#         break
#
#     # 단계 갱신
#     stage += 1
#
#     # 1. 한 칸 회전시키기
#     if cnt == 0:
#         arr = [arr[-1]] + arr[:-1]
#         for j in range(1, len(arr)):
#             if arr[j][0] > 0 and arr[j][1] == True:
#                 arr[j][0] -= 1
#     else:
#         for l in range(len(arr)-1, 0, -1):
#             arr[l][0] = arr[l-1][0]
#             if arr[l][0] > 0 and arr[l-1][1] == True:
#                 arr[l - 1][1] = False
#                 arr[l][1] = True
#                 arr[l][0] -= 1
#
#     # 2. n번 칸에서 내리기
#     arr[n-1][1] = False
#
#     print("올리기 전")
#     print(arr)
#
#     # 3. 0번 칸에서 로봇 올리기
#     if arr[0][0] > 0:
#         arr[0][1] = True
#         arr[0][0] -= 1
#
#     print("올린 후")
#     print(arr)
#
# print(stage)

# # 시도 2
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().strip().split())
# arr = list(map(int, input().strip().split()))
# robots = [False] * (2 * n)
# stage = 0
#
# while arr.count(0) < k:
# # for _ in range(10):
#     # 단계 갱신
#     stage += 1
#
#     # 0. 벨트 이동
#     arr = [arr[-1]] + arr[:-1]
#
#     # 1. 로봇들을 한 칸씩 이동시키기
#     for i in range(n, -1, -1):
#         if arr[i] > 0 and robots[i-1] == True and robots[i] == False:
#             robots[i-1] = False
#             robots[i] = True
#             arr[i] -= 1
#
#
#     # 2. n번 칸에서 내리기
#     robots[n-1] = False
#
#     # 3. 0번 칸에서 로봇 올리기
#     if arr[0] > 0:
#         robots[0] = True
#         arr[0] -= 1
#     # else:
#     #     robots[0] = False
#
#     print(arr)
#     print(robots)
#
# print(stage)

# 시도 3 - 문제 이해 후 다시
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
belts = list(map(int, input().strip().split()))
answer = 0
zeros = 0

# 내구도와 로봇 묶기
for i in range(len(belts)):
    belts[i] = [belts[i], False]    # 내구도, 로봇 존재 여부
    if belts[i] == 0:
        zeros += 1

while zeros < k:
    # # 내구도 0 개수 세기 - 시간 초과
    # zeros = 0
    # for belt in belts:
    #     if belt[0] == 0:
    #         zeros += 1
    # if zeros >= k:
    #     break

    answer += 1

    # 1. 벨트와 로봇 이동하기
    belts = [belts[-1]] + belts[:-1]

    # 1-1. n번째 칸이면 즉시 내리기
    belts[n-1][1] = False

    # 2. 로봇만 한 칸 더 이동시키기 (n에 가까운 칸부터)
    for i in range(n-1, 0, -1):
        if belts[i][0] > 0 and belts[i][1] == False and belts[i-1][1] == True:
            belts[i][1] = True
            belts[i-1][1] = False
            belts[i][0] -= 1
            if belts[i][0] == 0:
                zeros += 1

    # 2-1. n번째 칸이면 즉시 내리기
    belts[n-1][1] = False

    # 3. 로봇 0번째 칸에 올리기
    if belts[0][0] > 0:
        belts[0][1] = True
        belts[0][0] -= 1
        if belts[0][0] == 0:
            zeros += 1

print(answer)