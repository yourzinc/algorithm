N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = []

for i in range(N):
    room.append(list(map(int, input().split())))

answer = 0

# N, E, S, W
# 북 0- -> 서 3 -> 남 2 -> 동 1
dx = [ 0 , 1, 0, -1 ]
dy = [ -1, 0, 1, 0 ]

# 문제 조건
# d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

# 북, 서, 남, 동 
# dx = [ 0 , -1, 0, 1 ] 
# dy = [ -1, 0, 1, 0 ]

def rotate(nd):
    # nd = 0 -> 3
    # nd = 1 -> 0
    # nd = 2 -> 1
    # nd = 3 -> 2
    nd -= 1
    if nd == -1 : return 3
    return nd

nd = d
while True:
    # 현재 위치를 청소한다
    if room[r][c] == 0:
        answer +=1
        room[r][c] = 2

    # 현재 방향을 기준으로 왼쪽 방향 탐색
    flag = False
    
    for i in range(4):
        # nd = (d+1)%4    i와 1의 차이
        nd = rotate(nd) 
        nr = r + dy[nd]
        nc = c + dx[nd]

        if room[nr][nc] == 0:
            flag = True
            r = nr
            c = nc
            d = nd
            # 다시 while 문 반복
            break

    # 네 방향 모두 청소가 되어있거나 / 벽인 경우
    if not flag:
        
        nr = r - dy[d]
        nc = c - dx[d]

        # 뒤쪽 방향이 벽이라 후진도 못한다
        if room[nr][nc] == 1:
            break
        
        r = nr # 벽이 아닌 경우 업데이트
        c = nc 

print(answer)