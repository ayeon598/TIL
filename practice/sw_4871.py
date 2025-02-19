T = int(input())

def dfs(arr, start, visited):   # start에서 갈 수 있는 경로 찾기
    visited[start] = True
    for i in arr[start]:
        if not visited[i]:
            dfs(arr, i, visited)
    return visited

for t in range(1, T+1):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for j in line:
        arr[j[0]].append(j[1])
    for i in range(1, V + 1):
        arr[i].sort()
    visited = [False] * (V + 1)
    result = dfs(arr, S, visited)
    if result[G] == True: print(f'#{t} 1')
    else: print(f'#{t} 0')