# # 시도 1 - 시간 초과
# import sys
# input = sys.stdin.readline
#
# n, k, p, x = map(int, input().strip().split())
# answer = 0
#
# digit_dp = {
#     0: [True, True, True, False, True, True, True],
#     1: [False, False, True, False, False, True, False],
#     2: [True, False, True, True, True, False, True],
#     3: [True, False, True, True, False, True, True],
#     4: [False, True, True, True, False, True, False],
#     5: [True, True, False, True, False, True, True],
#     6: [True, True, False, True, True, True, True],
#     7: [True, False, True, False, False, True, False],
#     8: [True, True, True, True, True, True, True],
#     9: [True, True, True, True, False, True, True]
# }
#
# original_digits = list(map(int, str(x)))
# if len(original_digits) < k:
#     original_digits = [0] * (k - len(original_digits)) + original_digits
#
# for target in range(1, n+1):
#     target_digits = list(map(int, str(target)))
#     change_cnt = 0
#
#     # 최대 k자리의 숫자 보임 - 빈칸은 0으로 처리하기
#     if len(target_digits) < k:
#         target_digits = [0] * (k-len(target_digits)) + target_digits
#
#     continueTF = True
#     for digit in range(min(len(target_digits), k+1)):
#         for i in range(7):
#             if digit_dp[original_digits[digit]][i] != digit_dp[target_digits[digit]][i]:
#                 change_cnt += 1
#                 if change_cnt > p:
#                     continueTF = False
#                     break
#         if not continueTF:
#             break
#     else:
#         answer += 1
#
# print(answer-1)

# 시도 2 - 다 미리 세두기
import sys
input = sys.stdin.readline

n, k, p, x = map(int, input().strip().split())
answer = 0

change = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]

original_digits = list(map(int, str(x)))
or_len = len(original_digits)
if len(original_digits) < k:
    original_digits = [0] * (k - or_len) + original_digits

if or_len > k:
    print(0)
else:
    for target in range(1, n+1):
        change_cnt = 0
        can_make = True

        target_digits = list(map(int, str(target)))
        tar_len = len(target_digits)
        if len(target_digits) < k:
            target_digits = [0] * (k - tar_len) + target_digits

        for i in range(k):
            change_cnt += change[original_digits[i]][target_digits[i]]
            if change_cnt > p:
                can_make = False
                break

        if can_make:
            answer += 1

    print(answer-1)