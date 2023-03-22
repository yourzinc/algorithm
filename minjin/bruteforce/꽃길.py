import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
data = []
costs = []
for _ in range(n):
    data.append(list(map(int, input().strip().split())))

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def calc_point_cost(x, y):
    soil_cost = data[x][y]
    for d in range(4):
        soil_cost += data[x + dx[d]][y + dy[d]]
    return soil_cost

for x in range(1, n - 1):
    for y in range(1, n - 1):
        soil_cost = calc_point_cost(x, y)
        costs.append([soil_cost, (x, y)])
costs.sort()


def compatible(loc1, loc2):
    if abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1]) > 2:
        return True
    return False


def calc_min_cost(x, y):
    tmp_costs = deque(costs)
    cost = calc_point_cost(x, y)
    flowers = [[x, y]]
    while len(flowers) < 3:
        checking = tmp_costs.popleft()
        new_i, new_j = checking[1]
        for f in flowers:
            if not compatible(f, [new_i, new_j]):
                break
        else:
            flowers.append([new_i, new_j])
            cost += checking[0]
    return cost


min_cost = int(1e9)
for i in range(1, n - 1):
    for j in range(1, n - 1):
        min_cost = min(min_cost, calc_min_cost(i, j))

print(min_cost)
