from time import strftime,localtime

n = int(input())
arr = []
for i in range(n):
    team, time = input().split()
    arr.append([int(team),int(time.split(':')[0])*60 + int(time.split(':')[1])])
    
arr.append([-1,48*60]) #종료시간 추가

result = [0,0]
score= [0,0]
checktime = 0

for i in range(len(arr)):
    if arr[i][0] != -1 :
        if score[0]!=score[1]:
            result[score.index(max(score))]+= arr[i][1] - checktime
        score[arr[i][0]-1] += 1
        checktime = arr[i][1]
    else: #종료시간을 만나면
        if score[0]!=score[1]: #점수가 동점이아니면 result 갱신
            result[score.index(max(score))]+= arr[i][1] - checktime
        
for i in result:
    t = localtime(i)
    print(strftime('%M:%S',t))
