def dfs(arr, start, visited):
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            dfs(arr, i, visited)
    return visited

for _ in range(10):
    t, N = map(int, input().split())
    arr = [[] for _ in range(100)]
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        arr[lst[i]].append(lst[i+1])
    visited = [False] * (100)
    a = dfs(arr, 0, visited)
    if a[99] == True: print(f'#{t} 1')
    else: print(f'#{t} 0')