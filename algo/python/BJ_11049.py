def dp(arr, n):
    dat = [[0] * n for _ in range(n)]
    for i in range(1, N):
        for j in range(N):
            if i + j == N: break
            dat[j][i+j] = float('inf')
            for k in range(j, j+i):
                dat[j][j+i] = min(dat[j][j+i], dat[j][k] + dat[k+1][j+i] + arr[j][0]*arr[k][1]*arr[j+i][1])
    return dat[0][n - 1]

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
result = dp(arr, N)
print(result)
