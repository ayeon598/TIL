arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

y, x = map(int, input().split())

# 아래, 오른쪽 , 왼쪽, 오른쪽아래
dy = [1, 0, 0, 1]
dx = [0, 1, -1, 1]

max_v = float('-inf') # 음의 무한대

for i in range(4): # 아래, 오른쪽, 왼쪽, 오른쪽아래 (4방향)
    ny = y + dy[i]
    nx = x + dx[i]

    if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue

    if arr[ny][nx] > max_v: max_v = arr[ny][nx] # 최대값 갱신

print(max_v)