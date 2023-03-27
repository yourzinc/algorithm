import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 입력 받기
n = int(input())
s = input().strip()
nums = []
ops = []
for i in range(len(s)):
    if i % 2 == 0:
        nums.append(s[i])
    else:
        ops.append(s[i])

# 괄호 넣을 곳 선택하기
brackets = []
for cnt in range(len(ops)//2+1):
    combs = list(combinations([i for i in range(len(ops))],cnt))
    for com in combs:
        for i in range(len(com)-1):
            if com[i] == com[i+1] -1 or com[i] == com[i-1] + 1:
                break
        else:
            brackets.append(com)

# 괄호 넣을 곳들을 기반으로, deque로 순서대로 계산하기
max_value = int(-1e9)
for case in brackets:
    q = deque([nums[0]])
    for i in range(len(ops)):
        if i in case:
            tmp = q.pop()+ops[i]+nums[i+1]
            q.append(str(eval(tmp)))
        else:
            q.append(ops[i])
            q.append(nums[i+1])

    # queue 앞에서부터 계산하기
    tmp_value = q.popleft()
    while q:
        tmp_value = str(eval(tmp_value + q.popleft() + q.popleft()))
    max_value = max(int(tmp_value), max_value)

if n == 1:
    print(s)
else:
    print(max_value)