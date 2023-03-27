# # 시도 1
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# s = input().strip()
# t = input().strip()
#
# def add_a(str):
#     return str+"A"
#
# def add_b(str):
#     tmp = list(str+"B")
#     tmp.reverse()
#     return "".join(tmp)
#
# def solution():
#     if s == t:
#         return 1
#     q = deque([s])
#     while q:
#         checking = q.popleft()
#         result1 = add_a(checking)
#         result2 = add_b(checking)
#         if t in [result1, result2]:
#             return 1
#         if len(result1) > len(t):
#             break
#         q.append(result1)
#         q.append(result2)
#     return 0
#
# print(solution())


# 시도 2
s = list(input())
t = list(input())

def dfs(x):
    if s == x:
        return True
    if len(s) >= len(x):
        return False

    ans1, ans2 = False, False
    if x[-1] == "A":
        ans1 = dfs(x[:-1])
    if x[0] == "B":
        ans2 = dfs(x[1:][::-1])
    if True in [ans1, ans2]:
        return True

if dfs(t):
    print(1)
else:
    print(0)
