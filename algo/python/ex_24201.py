from collections import deque

N, M = map(int, input().split())
arr = []
d = [] * (N+1)
cnt = 0
for i in range(M):
    A, B = map(int, input().split())
    arr.append((A,B))
    d[A].append(B)
    d[B].append(A)
R, K = map(int, input().split())

q = deque()
used = [0] * (N+1)
q.append((R, 0))
used[R] = 1
while q:

# from collections import deque
#
# n, m = map(int, input().split())
# # 노드가 1부터 시작
# visited = [0] * 11
# # 인접행렬도 노드 번호가 1부터 시작
# MAP = [[0] * 11 for _ in range(11)]
# cnt = 0
#
# for i in range(m):
#     from_node, to_node = map(int, input().split())
#     # 인접행렬 -> 양방향 특징 : 대칭이다
#     MAP[from_node][to_node] = 1
#     MAP[to_node][from_node] = 1
#
# r, k = map(int, input().split())
#
#
# def bfs(node):
#     global cnt
#     q = deque()
#     # 시작노드 큐에 넣어준다. 시작노드 방문처리
#     q.append(node)
#     visited[node] = 1
#
#     while q:
#         # 1. 큐에서 뺀다
#         now = q.popleft()
#
#         # k이하면 counting(시작할때부터 1이니까 1을 빼준다)
#         if visited[now] - 1 <= k: cnt += 1
#
#         # bfs 특성상 level단위로 탐색 1칸... 2칸... 3칸...
#         if visited[now] - 1 > k:
#             break
#
#         # 2. 다음 갈 곳 예약걸기(1번노드부터)
#         for i in range(1, n + 1):
#             if MAP[now][i] == 0: continue
#             if visited[i] > 0: continue
#             # 방문처리(거리가 멀어질수록 1씩 증가)
#             visited[i] = visited[now] + 1
#             q.append(i)
#
#
# # start가 r
# bfs(r)
# print(cnt)
