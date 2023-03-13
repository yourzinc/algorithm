n = int(input())
ball = input()

#공의 개수가 적은 것을 옮기는 것이 유리하므로 일단 어떤 공의 개수가 더 적은지 센다.
rcount = ball.count('R')
bcount = ball.count('B')
ans = min(rcount, bcount)

#왼쪽으로 모으는 경우 
cnt = 0
for i in range(n): #젤 왼쪽에 있는 공기준으로 연속되는 개수 찾기
    if ball[i] != ball[0]: #ball[0]=R
        break
    cnt += 1
    
if ball[0] == 'R': #첫번째 공이 빨간공이면
    ans = min(ans, rcount - cnt) 
else:
    ans = min(ans, bcount - cnt)  
    
#오른쪽으로 모으는 경우
cnt = 0
for i in range(n-1, -1, -1): #오른쪽에서부터 연속되는 공 개수 찾기
    if ball[i] != ball[n - 1]:
        break
    cnt += 1

if ball[n - 1] == 'R': #맨뒤에 공이 빨간공이면
    ans = min(ans, rcount - cnt)
else:
    ans = min(ans, bcount - cnt)
       
print(ans)
