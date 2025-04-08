def find_max_Value(arr, K):
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(K+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif arr[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - arr[i-1][0]] + arr[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][K]

N, K = map(int, input().split())
arr = []
for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))
max_value = find_max_Value(arr, K)
print(max_value)
