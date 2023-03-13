n = int(input())

light = list(map(int, list(input())))
result = list(map(int, list(input())))

def first_change(now):
    cnt = 1 
    now[0] = 1 - now[0]
    now[1] = 1 - now[1]
    for i in range(1,n):
        if now[i-1] == result[i-1]:
            continue
        else:
            # 이전 전구와 스위치 전구의 상태를 바꾼다.
            cnt+=1
            now[i-1] = 1- now[i-1]
            now[i] = 1 - now[i]
            # 스위치 이후에 전구가 있다면 이후 전구의 상태를 바꾼다.
            if i < n-1:
                now[i+1] = 1 - now[i+1]
    
    if now == result:
        return cnt 
    return 1e9

def first_not_change(now):
    cnt = 0 
    for i in range(1,n):
        if now[i-1] == result[i-1]:
            continue
        else:
            # 이전 전구와 스위치 전구의 상태를 바꾼다.
            cnt+=1
            now[i-1] = 1- now[i-1]
            now[i] = 1 - now[i]
            # 스위치 이후에 전구가 있다면 이후 전구의 상태를 바꾼다.
            if i < n-1:
                now[i+1] = 1 - now[i+1]
    
    if now == result:
        return cnt 
    return 1e9

cnt1 = first_change(light[:])
cnt2 = first_not_change(light[:])
answer = min(cnt1,cnt2)
if answer ==1e9:
    answer = -1

print(answer)
