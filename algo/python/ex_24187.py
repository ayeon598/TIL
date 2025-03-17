from collections import deque

MAP = [
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
node = 'ACBQTPR'

q = deque()
q.append(0)
while q:
    now = q[0]
    q.popleft()
    print(node[now], end=' ')

    for i in range(7):
        if MAP[now][i] == 0: continue
        next = i
        q.append(next)