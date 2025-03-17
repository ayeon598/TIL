def dfs(start):
    global visited
    visited.append(start)
    for i in range(6):
        if MAP[start][i] == 1:
            dfs(i)

MAP = [
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
    ]
visited = []
dfs(0)
print(*visited)