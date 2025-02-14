N, M = map(int, input().split())
K = int(input())
arr = [list(map(str, input())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '@':
            for l in range(4):
                for k in range(K+1):
                    dy = [-1, 1, 0, 0]
                    dx = [0, 0, -1, 1]
                    ny = i + k * dy[l]
                    nx = j + k * dx[l]
                    if ny < 0 or nx < 0 or ny >= N or nx >= M or arr[ny][nx] == '@': continue
                    if arr[ny][nx] == '#': break
                    arr[ny][nx] = '%'

for i in range(N):
    for j in range(M):
        arr[i][j] = arr[i][j].replace('@', '%')
        print(arr[i][j], end='')
    print()