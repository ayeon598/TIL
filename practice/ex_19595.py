arr = [['_'] * 5 for _ in range(4)]

for _ in range(2): # 좌표를 2번 입력
    y, x = map(int, input().split())
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    for i in range(8): # 방향이 총 8방향
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
        arr[ny][nx] = '#'

for row in arr:
    temp = row
    print(*row)