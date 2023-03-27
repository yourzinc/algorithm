import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().strip().split()))
ops = list(map(int, input().strip().split()))

max_value = int(-1e9)
min_value = int(1e9)

def dfs(depth, value, plus, minus, multiply, divide):
    global max_value, min_value
    if depth == n:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    if plus:
        dfs(depth+1, value + nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, value - nums[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, value * nums[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(value/nums[depth]), plus, minus, multiply, divide-1)
        # int(value/nums[depth]) 주의!

dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(max_value)
print(min_value)