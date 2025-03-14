MAP = [
    [0, 2, 6, 3, 0, 0],
    [2, 0, 7, 4, 0, 0],
    [6, 7, 0, 0, 0, 0],
    [3, 4, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 7],
    [0, 0, 0, 0, 0, 0],
]

used = [0] * 6

def dfs(now):
    print(now, end = ' ')
    for i in range(6):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue # 방문기록이 되어있는 노드는 다시 방문하지 마라
        used[i] = 1 # 방문기록
        dfs(i)
        used[i] = 0

dfs(4)