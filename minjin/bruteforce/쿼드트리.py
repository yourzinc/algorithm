import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
raw_data = []
for _ in range(n):
    raw_data.append(list(input().strip()))

def make_zip(data):
    cnt_0 = 0
    cnt_1 = 0
    for row in range(len(data)):
        cnt_0 += data[row].count("0")
        cnt_1 += data[row].count("1")
    if cnt_0 == 0:
        return "1"
    elif cnt_1 == 0:
        return "0"
    elif len(data) == 2:
        return "(" + "".join(data[0]) + "".join(data[1]) + ")"
    else:
        part1, part2, part3, part4 = [], [], [], []
        half = len(data) // 2
        for i in range(half):
            part1.append(data[i][:half])
            part2.append(data[i][half:])
            part3.append(data[half+i][:half])
            part4.append(data[half+i][half:])
        return "(" + make_zip(part1) + make_zip(part2) + make_zip(part3) + make_zip(part4) + ")"


print(make_zip(raw_data))