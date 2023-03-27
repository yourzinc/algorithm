# 3/25 토 6:46 - 7:01
# [BOJ] 연산자 끼워넣기

import sys
input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
o1, o2, o3, o4 = map(int, input().split()) # +, -, x, /

global max_value, min_value

max_value = -1e9
min_value = 1e9

def solution(index, o1, o2, o3, o4, result):

    if index == N-1:
        global max_value, min_value

        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return
    
    if o1 > 0:
        solution(index+1, o1-1, o2, o3, o4, result + number[index+1] )
    if o2 > 0:
        solution(index+1, o1, o2-1, o3, o4, result - number[index+1] )
    if o3 > 0:
        solution(index+1, o1, o2, o3-1, o4, result * number[index+1] )
    if o4 > 0:
        if result < 0:
            result = (result * (-1) // number[index+1]) * (-1)
        else:
            result = result //  number[index+1]
        solution(index+1, o1, o2, o3, o4-1, result)

solution(0, o1, o2, o3, o4, number[0])
print(max_value)
print(min_value)