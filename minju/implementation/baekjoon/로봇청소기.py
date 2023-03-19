import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]    
    
ans = 0
def clean(x, y, d):
    global ans
    if arr[x][y] == 0: #청소안한구역이면
        arr[x][y] = 2 #청소시킴 
        ans += 1 #카운트
    for _ in range(4): #현재 위치에서 4칸 탐색 
        nd = (d + 3) % 4 
        nx = x + dx[nd]
        ny = y + dy[nd]
        if arr[nx][ny] == 0: #마찬가지로 청소 안했으면 
            clean(nx, ny, nd) #다시 청소 시킴 
            return
        d = nd
        
    nd = (d + 2) % 4 #4방향을 돌아도 발견하지 못하면, 후진
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 1: #벽을 만나면 종료
        return
    clean(nx, ny, d) #벽이 아니면 이동해서 다시 돌리기
    
clean(r,c,d)
print(ans)
