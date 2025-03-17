from collections import deque

node = [5, 3, 1, 2, 4, 0, 6]
lst = list([] for _ in range(7))
lst[0] = [1, 2]
lst[1] = [3]
lst[2] = [4]
lst[4] = [5, 6]

q = deque()
q.append(0)

while q:
    now = q[0]
    q.popleft()
    print(node[now], end = ' ')

    for i in range(len(lst[now])):
        next = lst[now][i]
        q.append(next)