# [BOJ] 행렬 
# https://www.acmicpc.net/problem/1080 

N, M = map(int, input().split())

arr = []
arr2 = []

for i in range(N):
    arr.append(list(map(int, input())))

for i in range(N):
    arr2.append(list(map(int, input())))

count = 0

def check():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != arr2[i][j]:
                return False
    return True
    
if check():
    print(count)
    
elif N < 3 or M < 3:
    print(-1)
    
else:
    for i in range(N-2):
        for j in range(M-2):
    
            if arr[i][j] != arr2[i][j]:
                # 뒤 집 기
                for a in range(3):
                    for b in range(3):
                        if i+a < N and j+b < M:
                            arr[i+a][j+b] = (arr[i+a][j+b] + 1) %2
                            flag = True
                count += 1
    if check():
        print(count)
    else:
        print(-1)