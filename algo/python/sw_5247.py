from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = set([N])
    min_cnt = 0
    queue = deque()
    queue.append((N, 0))

    while queue:
        now, cnt = queue.popleft()

        if now == M:
            min_cnt = cnt
            break

        next = [
            (now + 1, "+1"),
            (now - 1, "-1"),
            (now * 2, "*2"),
            (now - 10, "-10")
        ]

        for i in next:
            next_value = i[0]
            if 1 <= next_value <= 1000000 and next_value not in visited:
                queue.append((next_value, cnt + 1))
                visited.add(next_value)

    print(f"#{t} {min_cnt}")