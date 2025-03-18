# from collections import deque
#
# node = 'ABCDE'
# MAP = [
#     [0, 1, 0, 0, 1],
#     [0, 0, 0, 1, 1],
#     [1, 0, 0, 0, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0]
# ]
# s, e = map(int, input().split())
# q = deque()
# q.append(s)
# visited = [0] * 5
# min_cnt = float('inf')
# cnt = 0
# while q:
#     now = q[0]
#     q.popleft()
#     visited[now] = 1
#
#     if now == e:
#         break
#
#     for i in range(5):
#         if MAP[now][i] == 0: continue
#         if visited[MAP[now][i]] == 1: continue
#         next = i
#         cnt += 1
#         q.append(next)
# print(cnt)

from collections import deque

MAP = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

q = deque()
used = [0] * 10
start, end = map(int, input().split())
# start를 q에 넣는다
# level 도 같이 넣어준다
q.append((start, 0))
# 시작 노드 방문처리
used[start] = 1

while q:
    # 1. 큐에서 뺸다(탐색)
    now, level = q[0]
    q.popleft()

    # now(현재 탐색하는 노드)가 end에 도착했을때 break
    if now == end:
        print(level)
        break

    # 2. 다음 갈 곳 예약 걸기(큐에 등록)
    for i in range(5):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        q.append((i, level + 1))