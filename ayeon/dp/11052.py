# [BOJ] 카드 구매하기

N = int(input())
p = list(map(int, input().split()))

dp = [0]*N # dp[i] = i-1 개의 카드를 구매하기 위해 지불하는 최댓값

dp[0] = p[0]

for i in range(1, N):
    dp[i] = p[i]
    for j in range((i+1)//2):
        dp[i] = max(dp[i], dp[j]+dp[i-j-1])

print(dp[N-1])