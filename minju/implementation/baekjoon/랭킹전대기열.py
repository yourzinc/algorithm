import sys
input = sys.stdin.readline

p, m = map(int, input().split())
arr = []
for i in range(p):
    l, n = input().split()
    arr.append([int(l),n])
    
result = [[arr[0]]]   
for i in range(1,len(arr)):
    check = False
    for j in range(len(result)):
        if len(result[j]) < m:
            if result[j][0][0]-10 <= arr[i][0] <= result[j][0][0]+10:
                result[j].append(arr[i])
                check = True 
                break
    if check == False:
        result.append([arr[i]])
        
for i in range(len(result)):
    if len(result[i]) == m:
        print('Started!')
        result[i].sort(key=lambda x :(x[1]))
        for j in result[i]:
            print(*j)
    else:
        print('Waiting!')
        result[i].sort(key=lambda x :(x[1]))
        for j in result[i]:
            print(*j)
