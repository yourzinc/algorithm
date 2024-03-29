import sys
input = sys.stdin.readline

n = int(input())
g = [list(map(int, input().split())) for i in range(n)]
visited = [[0] * n for i in range(n)]
answer = 99999999
total = 0

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

# 본래 자리를 포함한 4방향에 이미 꽃을 심었다면
# False를 아니면 True를 리턴
def check(a, b):
    for i in range(5):
        x = a + di[i]
        y = b + dj[i]
        if visited[x][y] == 1:
            return False
    return True

def recur(cur):
    global total, answer
    
    # 꽃을 3개 다 심었을 때 최소 코스트 갱신
    if cur == 3:
        answer = min(answer, total)
        return
 
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            # 5 공간에 이미 심지 않았다면
            if check(i, j):
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 1
                    total += g[x][y]
 
                recur(cur + 1)
                
                # 다음 재귀를 위해 초기화
                for k in range(5):
                    x = i + di[k]
                    y = j + dj[k]
                    visited[x][y] = 0
                    total -= g[x][y]
                    
recur(0)
print(answer)
