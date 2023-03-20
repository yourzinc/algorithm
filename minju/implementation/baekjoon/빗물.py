h, w = map(int, input().split())
arr = [[0 for j in range(w)] for i in range(h)] #초기 배열
block = list(map(int, input().split())) #블럭위치 입력받음

for i in range(len(block)): #블럭 위치에 맞게 배열에 1입력해줌
    for j in range(1,block[i]+1):
        arr[h-j][i] = 1

result = 0
for i in range(len(arr)):
    if arr[i].count(1) < 2: #행에 1이 1개 이하이면 pass한다 (물이 막아지지 않으니까)
        continue 
    else:  #2개 이상이면
        bound = [j for j, x in enumerate(arr[i]) if x == 1] #해당 1위치를 찾는다
        for k in range(1,len(bound)): #1위치에 따라 경계값을 구해줌
            if bound[k] - bound[k-1] != 1: #경계값이 1이 아닌 경우만 더해준다 (경계값이 1이면 블럭이 붙어있는거니까!)
                result += bound[k] - bound[k-1]-1   
                
print(result)
