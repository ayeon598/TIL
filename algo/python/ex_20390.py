def min_route(start):
    global cnt
    min_num = float('inf')
    min_index = []
    for i in range(4):
        dy, dx = d[i]
        y = start[0] + dy
        x = start[1] + dx
        if y < 0 or x < 0 or y >= N or x >= N: continue
        if arr[y][x] > min_num: continue
        elif arr[y][x] < min_num:
            min_num = arr[y][x]
            min_index.clear()
            min_index.append((y, x))
        else: min_index.append((y, x))
    cnt += min_num
    for i in min_index:
        if i == end:
            break
        min_route(i)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = (0, 0)
    end = (N-1, N-1)
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = arr[0][0]
    min_route(start)
    print(f'#{t} {cnt}')
