def dfs(start):
    global visited
    visited.append(start)
    for i in range(6):
        if MAP[start][i] != 0:
            if i in visited: continue
            dfs(i)

MAP = [
    [0, 2, 6, 3, 0, 0],
    [2, 0, 7, 4, 0, 0],
    [6, 7, 0, 0, 0, 0],
    [3, 4, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 7],
    [0, 0, 0, 0, 0, 0]
]
visited = []
dfs(4)
print(*visited)