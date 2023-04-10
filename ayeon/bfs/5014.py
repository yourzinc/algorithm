# [BOJ] 스타트링크

# 건물 F 층 
# 스타트링크 위치 G 층
# 강호 위치 S 층

# U는 위로 U 칸 
# D는 아래로 D 칸

# 버튼을 적어도 몇 번 눌러야 하는지 출력
# 갈 수 없다면 "use the stairs" 출력

from collections import deque

F, S, G, U, D = map(int, input().split())

m = [-1]*(F+1)

def bfs(F,S,G,U,D):
    q = deque([])
    q.append(S)
    m[S] = 0

    while q:
        x = q.popleft()
        
        if x == G:
            return True
        
        for nx in [x+U, x-D]:
            if nx <= 0 or nx > F:
                continue
            
            if m[nx] == -1:
                q.append(nx)
                m[nx] = m[x] + 1
        
    return False

if bfs(F,S,G,U,D):
    print(m[G])
else:
    print("use the stairs")