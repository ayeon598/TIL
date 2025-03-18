from collections import deque

node = 'ABCDE'
lst = list([] for _ in range(5))
lst[0] = [1, 2]
lst[1] = [0, 2]
lst[2] = [0, 1, 3]
lst[3] = [2, 4]
lst[4] = [3]

N = int(input())
q = deque()
q.append(N)
visited = [0] * 5
while q:
    now = q[0]
    q.popleft()
    if visited[now] == 1: continue
    visited[now] = 1
    print(node[now], end=' ')
    for i in range(len(lst[now])):
        if visited[lst[now][i]] == 1: continue
        next = lst[now][i]
        q.append(next)