def cal_length(arr):
    l = len(arr)
    dp = [1 for _ in range(l)]
    for i in range(1, l):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    dp.sort()
    return dp[-1]

N = int(input())
arr = list(map(int, input().split()))
num = cal_length(arr)
print(num)