# [BOJ] 텀 프로젝트

# 4/4 5:20 - 5:56

# 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택

# 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산

# 숫자고르기 문제와 유사

# dfs
# arr[3][0] = 4, arr[3][1] = 7
# arr[6][0] = 7, arr[6][1] = 6
# arr[5][0] = 6, arr[5][1] = 4

# 인접 노드 = arr[i][1] == arr[j][0]

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())

while T:
    n = int(input())
    arr = list(map(int, input().split()))
    
    global answer
    answer = [False]*n

    
    for i in range(n):
        arr[i] = [ i+1, arr[i] ]

    def dfs(i):
        # i 번째 노드 방문
        # team1 : 선택한 학생들
        # team2 : 선택 받은 학생들

        flag = False # 방문 확인
        team1[i] = True # 선택한 학생 추가

        # 인접 노드에 대해서 탐색
        for k in range(n):
            if arr[i][1] == arr[k][0] and not team2[k]:
                flag = True

                # 방문
                team2[k] = True
                dfs(k)

                # Roll back
                team2[k] = False

        
        if not flag:
            # 인접한 노드 중 방문할 노드가 없다
            if team1 == team2:
                # 팀을 이룰 수 있다
                
                for i in range(len(team1)):
                    if team1[i] == True:
                        answer[i] = True

            else:
                # 팀을 이룰 수 없다
                return


    for i in range(n):
        if not answer[i] :
            team1 = [False]*n
            team2 = [False]*n
            dfs(i)
    
    print(answer.count(False))
    T-=1


############### SET

global answer
answer = set([])

T = int(input())

while T:
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n):
        arr[i] = [ i+1, arr[i] ]

    def dfs(i, team1, team2):
        # i 번째 노드 방문
        # visited : 방문 처리 list
        # team1 : 선택한 학생들 set
        # team2 : 선택 받은 학생들 set

        flag = False # 방문 확인
        team1.add(i+1) # 선택한 학생 추가

        # 인접 노드에 대해서 탐색
        for k in range(n):
            if arr[i][1] == arr[k][0] and k+1 not in answer and k+1 not in team2:
                flag = True

                # 방문
                team2.add(k+1)
                dfs(k, team1, team2)

                # Roll back
                team2.remove(k+1)


        if not flag:
            # 인접한 노드 중 방문할 노드가 없다
            if set(team1) == set(team2):
                # 팀을 이룰 수 있다
                print("POSSIBLE i", i, "team1", team1, "team2", team2)
                global answer
                answer = answer | set(team1)

            else:
                # 팀을 이룰 수 없다
                print("POSSIBLE i", i, "team1", team1, "team2", team2)
                return


    for i in range(n):
        dfs(i, set([]), set([]))

    print(n-len(answer))
    
    T-=1