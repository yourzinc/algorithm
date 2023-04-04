import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
for k in range(n): #거쳐가는 것이 제일 먼저 나와야한다
    for i in range(n):
        for j in range(n):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] =1
                
for i in range(len(arr)):
    print(' '.join(map(str,arr[i])))
