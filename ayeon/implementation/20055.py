from collections import deque

answer = 1

N, K = map(int, input().split()) # 내구도가 0인 칸의 개수가 K개 이상이면 종료
A = deque(list(map(int, input().split())))

k = 0 # 내구도가 0인 칸의 개수

B = deque([False]*N) # 로봇

while True:

    # 회전
    A.appendleft(A.pop())
    B.pop() # 맨 끝 내리기
    B.appendleft(False)

    # 이동

    for i in range(N-1, 0, -1):
        # B[i-1] : 지금 있는 위치
        # B[i] : 다음칸
        
        # 내리는 위치에 도달하면 그 즉시 내린다
        if i == N-1: 
            B[i] = False
                
        if B[i-1] and not B[i] and A[i] > 0:
            # 지금 로봇이 있고, 다음 칸에 로봇이 없으며, 그 칸의 내구도가 0 보다 크다
            B[i] = True
            B[i-1] = False
            A[i] -= 1

            if A[i] == 0:
                k += 1
                A[i] = -1

        # 이동할 수 없다면 가만히 있는다
    
    # 올리기
    if A[0] > 0:
        B[0] = True
        A[0] -= 1

        if A[0] == 0:
            k += 1
            A[0] = -1

    
    # 내구도 확인
    if k >= K:
        break

    answer += 1

print(answer)