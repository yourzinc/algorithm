# 오늘의 교훈
# 최대한 함수로 쪼개기

import sys
input = sys.stdin.readline

n = int(input())
switches = [-1] + list(map(int, input().strip().split()))
k = int(input())

def change(x):
    if switches[x] == 1:
        switches[x] = 0
    else:
        switches[x] = 1

def boy(num):
    for i in range(num, n+1):
        if i % num == 0:
            change(i)
            # switches[i] ^= 1
def girl(num):
    change(num)
    # switches[number] ^= 1
    left, right = num-1, num+1
    while left >= 1 and right <= n:
        if switches[left] == switches[right]:
            change(left)
            change(right)
            left -= 1
            right += 1
        else:
            break

for _ in range(k):
    gender, num = map(int, input().strip().split())
    if gender == 1:
        boy(num)
    else:
        girl(num)

for i in range(1, n+1, 20):
    print(*switches[i:i+20])

# for i in range(1, n+1):
#     print(switches[i], end = " ")
#     if i % 20 == 0:
#         print()