from collections import deque

def bfs(arr, S, G, V):
    queue = deque([(S, 0)])
    visited = [False] * (V + 1)
    visited[S] = True

    while queue:
        node, dist = queue.popleft()

        if node == G:
            return dist

        for next_node in arr[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + 1))

    return 0

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)  # 무방향 그래프이므로 양쪽 모두 추가하기

    S, G = map(int, input().split())

    result = bfs(arr, S, G, V)
    print(f'#{t} {result}')
