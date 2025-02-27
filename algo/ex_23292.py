arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

y, x = map(int, input().split())

# 자기자신, 위왼쪽, 위오른쪽, 아래왼쪽, 아래오른쪽
dy = [0, -1, -1, 1, 1]
dx = [0, -1, 1, -1, 1]

# gop = arr[y][x] # 자기자신
gop = 1

for i in range(5):
    ny, nx = y + dy[i], x + dx[i]
    # 범위벗어나면 반복문 처음으로 돌아가기
    if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
    gop *= arr[ny][nx]

print(gop)