n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value = -int(1e9)
min_value = int(1e9)

def dfs(depth, num, add, sub, mul, div):
    global max_value, min_value
    if depth == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
    else:
        if add:
            dfs(depth+1, num+data[depth], add-1, sub, mul, div)
        if sub:
            dfs(depth+1, num-data[depth], add, sub-1, mul, div)
        if mul:
            dfs(depth+1, num*data[depth], add, sub, mul-1, div)
        if div:
            dfs(depth+1, int(num/data[depth]), add, sub, mul, div-1)

dfs(1, data[0], add, sub, mul, div)

print(max_value)
print(min_value)
