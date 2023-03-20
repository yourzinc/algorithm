N, M = map(int, input().split())

A = [list(map(int,list(input()))) for _ in range(N)]
B = [list(map(int,list(input()))) for _ in range(N)]

def reverse(x, y):
    for i in range(x, x+3): #현재 위치 기준에서 3by3행렬을 다 돌아서 뒤집어버림
        for j in range(y, y+3):
          A[i][j] = 1 - A[i][j]

def check():
  for i in range(N):
    for j in range(M):
      if A[i][j] != B[i][j]:
        return False
  
  return True


count = 0
for i in range(N-2):
  for j in range(M-2):
    if A[i][j] != B[i][j]: #현재 접근한 위치에서 값이 다르면 reverse함수 수행 
      reverse(i, j)
      count += 1

if check(): #전체 행렬이 다 같은지 확인
  print(count)
else:
  print("-1")
