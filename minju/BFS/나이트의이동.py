from collections import deque

# 이동할 방향
dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

# BFS 소스코드 구현
def bfs():
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x1, y1)) #현재 위치 좌표
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 8가지 방향으로의 위치 확인
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= m or ny < 0 or ny >= m:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1 #그래프자체에 거리 갱신
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[x2][y2] - 1

n = int(input()) #테스트케이스 개수

for i in range(n):
    m = int(input())
    graph = [[0]*m for _ in range(m)]
    x1, y1 = map(int, input().split()) #시작지점
    x2, y2 = map(int, input().split()) #종료지점
    graph[x1][y1] = 1
    # BFS를 수행한 결과 출력
    print(bfs())
