def dfs(now):
    if arr[now] == 0: return # 백트래킹

    dfs(now*2)
    print(arr[now], end='')
    dfs(now*2+1)

for t in range(1, 11):
    N = int(input())
    arr = [0] * 120
    for _ in range(N):
        lst = list(input().split())
        index = int(lst[0])
        arr[index] = lst[1]
    print(f'#{t}', end=' ')
    dfs(1)
    print()