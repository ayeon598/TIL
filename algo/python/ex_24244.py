import heapq

N, M, K = map(int, input().split())
A, B = map(int, input().split())
lst = []
for _ in range(M):
    f, t, c = map(int, input().split())

for _ in range(K):
    p = int(input())

# # 강사님 코드
# import heapq
#
# def dijkstra(start):
#     result = [float('inf')] * (N + 1)
#     result[start] = 0
#     pq = [(0, start)] # 시작 노드
#
#     while pq:
#         price, now = heapq.heappop(pq)
#
#         if result[now] < price: continue
#
#         # for i in range(n):
#         #     if MAP[now][i] == 0: continue
#         #     next_price = MAP[now][i]
#         for i, next_price in graph[now]:
#             price_sum = price + next_price
#             if result[i] > price_sum:
#                 result[i] = price_sum
#                 heapq.heappush(pq, (price_sum, i))
#
#     return result
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, E = map(int, input().split())
#     # MAP = [[0] * (N + 1) for _ in range(N + 1)]
#     graph = [[] for _ in range(N + 1)]
#
#
#     for _ in range(E):
#         s, e, w = map(int, input().split())
#         # MAP[s][e] = w  # start부터 end까지 단방향, 가중치 w
#         graph[s].append((e, w))
#
#     result = dijkstra(0)
#     print(f'#{tc} {result[N]}')