import sys

n = int(input())

graph = [] # 그래프 입력받기
for i in range(n):
    graph.append(list(map(int,input())))

def tree(x,y,n):
    if n == 1: # 최소 사각형인 경우 바로 추가
        answer.append(graph[x][y])
        return
    
    # 기준이 되는 숫자(사각형 왼쪽 맨 위)
    stand = graph[x][y]
    for i in range(x,x+n): # 범위 유의
        for j in range(y,y+n):
            # 기준과 다른 숫자가 나오면
            if graph[i][j] != stand:
                n //= 2 # 4분할 탐색
                answer.append('(')
                tree(x,y,n) # 왼쪽 위
                tree(x,y+n,n) # 오른쪽 위
                tree(x+n,y,n) # 왼쪽 아래
                tree(x+n,y+n,n) # 오른쪽 아래
                answer.append(')')
                return
    
    # 사각형이 한 숫자로만 이루어진 경우
    answer.append(stand)
    return

answer = []
tree(0,0,n) # (0,0)에서 시작

# answer의 모든 원소를 공백 없이 출력
print(*answer,sep='')
