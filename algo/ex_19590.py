N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
result = 0

for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(K):
            for l in range(4):
                dy = [-1, -1, 1, 1]
                dx = [-1, 1, -1, 1]
                ny = i + (k+1) * dy[l]
                nx = j + (k+1) * dx[l]
                if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
                cnt += arr[ny][nx]
        if result < cnt:
            result = cnt
print(result)