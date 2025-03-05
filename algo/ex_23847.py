bt = [0] * 100
bt[1] = 9
bt[2] = 4   # 9의 왼쪽 자식
bt[3] = 12  # 9의 오른쪽 자식
bt[4] = 3   # 4의 왼쪽 자식
bt[5] = 6   # 4의 오른쪽 자식
bt[7] = 15  # 12의 오른쪽 자식
bt[14] = 13 # 15의 왼쪽 자식
bt[15] = 17 # 15의 오른쪽 자식

def dfs(now):
    if bt[now] == 0: return # 백트래킹

    print(bt[now], end=' ')
    dfs(now * 2)
    dfs(now * 2 + 1)

dfs(1)