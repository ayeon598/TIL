from collections import deque

def bfs(start, end, arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start[0], start[1], 0)])    # 현재 위치 + 거기까지 간 거리
    visited = set([(start[0], start[1])])   # 방문한 곳

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == (end[0], end[1]):
            return dist - 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if (nx, ny) not in visited and arr[nx][ny] != 1:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    return 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    start = ()
    end = ()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)
            elif arr[i][j] == 3:
                end = (i, j)

    result = bfs(start, end, arr)
    print(f"#{t} {result}")