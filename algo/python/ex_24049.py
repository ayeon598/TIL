def dfs(start):
    global visited
    visited.append(start)
    for i in LIST[start]:
        if i in visited: continue
        dfs(i)

LIST = [[1, 3], [2], [0, 3], [2]]
visited = []
dfs(0)
for i in visited:
    print(i)