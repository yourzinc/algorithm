# [BOJ] 쿼드트리

# N * N 배열

import sys
input = sys.stdin.readline

def dfs(i, j, length):
    # i 시작 지점
    # j 시작 지점
    # length 길이

    if length < 1:
        return
    else:
        # case check
        first_value = m[i][j]

        for ii in range(length):
            for jj in range(length):
                if first_value != m[i+ii][j+jj] :  
                    first_value = -1
                    break

        # 1) 0만 있는 경우
        if first_value == 0:
            s.append('0')
            return
        
        # 2) 1만 있는 경우
        elif first_value == 1:
            s.append('1')
            return
        
        # 3) 0,1 섞여있는 경우
        else: 

            s.append('(')
            # 왼쪽 위
            dfs(i, j, length//2)

            # 오른쪽 위
            dfs(i, j+length//2, length//2)

            # 왼쪽 아래
            dfs(i+length//2, j, length//2)

            # 오른쪽 아래
            dfs(i+length//2, j+length//2, length//2)
            s.append(')')

    


s = []

n = int(input())
m = []

for _ in range(n):
    m.append(list(map(int, input())))

dfs(0, 0, n)
answer = ''
for i in s:
    answer += i
print(answer)