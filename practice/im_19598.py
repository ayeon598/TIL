T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    cnt = []
    for i in range(N):
        for j in range(N):
            sum_virus = 0
            sum_virus += arr[i][j]
            for k in range(1, P+1):
                for l in range(4):
                    y = i + dy[l] * k
                    x = j + dx[l] * k
                    if y < 0 or x < 0 or y > N-1 or x > N-1: continue
                    sum_virus += arr[y][x]
            cnt.append(sum_virus)
    print(f'#{t} {max(cnt)}')