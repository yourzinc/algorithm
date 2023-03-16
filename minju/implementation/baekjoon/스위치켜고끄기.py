import sys
input = sys.stdin.readline
n = int(input())
switch = list(map(int, input().split()))
switch.insert(0,0) #switch번호를 문제에 나오는 대로 풀고 싶어서 맨앞에 0을 추가해줌
s = int(input())

arr = []
for i in range(s):
    arr.append(list(map(int, input().split())))
    
for i in range(s):
    if arr[i][0] == 1: #남학생일 경우
        for j in range(arr[i][1],n+1,arr[i][1]):
            switch[j] = 1 - switch[j]
    else: #여학생의 경우
        front = 0 #범위를 저장해줄 앞부분
        back = 0 #범위를 저장해줄 뒷부분
        x = 1
        while (arr[i][1]-x > 0 and arr[i][1]+x < n+1):
            if switch[arr[i][1]-x] == switch[arr[i][1]+x]:
                front = arr[i][1]-x
                back = arr[i][1]+x
                x = x + 1
            else:
                break
                
        if front!=0 and back !=0: #범위가 존재한다면 그 범위 내에서 스위치 반전시킴    
            for j in range(front,back+1):
                switch[j] = 1 - switch[j]
        else: #범위가 존재하지 않는다면 해당 번호 스위치만 반전 시킴
            switch[arr[i][1]] = 1 - switch[arr[i][1]]
            
#출력
cnt = 0 
for i in range(1,len(switch)):
    if cnt == 20: #20개씩 출력하기 위함
        print()
        print(switch[i], end = ' ')
        cnt = 0
    else:
        print(switch[i], end = ' ')
    cnt += 1
