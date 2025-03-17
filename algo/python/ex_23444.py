def area(arr, e, f, a):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    for k in range(4):
        for c in range(a):
            y = e + dy[k] * (c+1)
            x = f + dx[k] * (c+1)
            if y < 0 or x < 0 or y > 9 or x > 9: continue
            if arr[y][x] == 0: arr[y][x] = -1
            elif arr[y][x] != -1: break
    return arr


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(10)]
    cnt = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1: area(arr, i, j, 1)
            elif arr[i][j] == 2: area(arr, i, j, 2)
            elif arr[i][j] == 3: area(arr, i, j, 3)
    for i in arr:
        cnt += i.count(0)
    print(f'#{t} {cnt}')
