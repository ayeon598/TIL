def dp(n):
    dp = [0] * (n+1)
    dp[10] = 1
    dp[20] = 3
    
    for i in range(30, n+1, 10):
        dp[i] = dp[i-10] +2 * dp[i-20]
    return dp[n]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t} {dp(N)}')