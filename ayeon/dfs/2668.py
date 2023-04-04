# [BOJ] 숫자고르기

# 첫째 줄에서 숫자를 적절히 뽑으면,
# 그 뽑힌 정수들이 이루는 집합과, 
# 뽑힌 정수들의 바로 밑의 둘째 줄에 들어있는 정수들이 이루는 집합이 일치한다.

# 정수들을 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램을 작성

# arr[0][0] = a, arr[0][1] = b 라고 할 때,
# 인접 노드 : arr[1][0] = b 

# 인접 노드가 없다면? return False
# 인접 노드가 있다면? dfs()

N = int(input())
arr = []

for i in range(N):
    arr.append((i+1, int(input())))

visited = [False]*(N)

global answer
answer = set([])
first = set([])
second = set([])

def dfs(i, first, second):
    # arr[i] 노드 방문
    
    # first : 첫째 줄
    # second : 둘째 줄 

    flag = False

    # 인접 노드
    for a1, a2 in arr:
        if arr[i][1] == a1 and not visited[a1-1] :
            flag = True
            # b = arr[new][0] 인 방문하지 않은 인접노드

            visited[a1-1] = True # 방문처리
            first.add(a1)
            second.add(a2)
            dfs(a1-1, first,second) # dfs

            visited[a1-1] = False # Rollback
            first -= {a1}
            second -= {a2}
        

    if not flag:
        # 새롭게 방문할 노드 없음
        if first == second:
            global answer
            answer = answer | first
    else:
        return

for i in range(N):
    dfs(i, first, second)

answer = list(answer)
answer.sort()

print(len(answer))
for a in answer:
    print(a)
