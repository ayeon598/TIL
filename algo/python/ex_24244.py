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
#     result = [float('inf')] * (n + 1)
#     result[start] = 0
#     # pq초기화 (비용, 노드)
#     pq = [(0, start)]
#     while pq:
#         # 1. 힙에서 뺀다
#         cost, node = heapq.heappop(pq)
#         # result배열의 값보다 더 큰값이면 continue
#         if result[node] < cost: continue
#         # 2. 다음 노드 예약 걸기(힙등록)
#         for next_node, next_cost in graph[node]:
#             next_cost = cost + next_cost # 가중치가 누적
#             # result 배열의 값보다 작은값이 나왔다 ---> 갱신
#             if result[next_node] > next_cost:
#                 result[next_node] = next_cost
#                 heapq.heappush(pq, (next_cost, next_node))
#
#     print(result[destination])
#
#
#
# n, m, k = map(int, input().split())
# start, destination = map(int, input().split())
# # 인접 리스트(빈배열초기화)
# graph = [[] for _ in range(n + 1)]
# # 간선 정보 - 양방향
# for _ in range(m):
#     s, e, cost = map(int, input().split())
#     graph[s].append((e, cost))
#     graph[e].append((s, cost)) # 양방향 그래프
#
# # 첫 번째 상태
# dijkstra(start)
#
#
# # k번 반복해서 간선 비용을 증가
# for _ in range(k):
#     increase = int(input())
#     # 모든 간선의 비용이 증가
#     for y in range(1, n + 1):
#         for x in range(len(graph[y])):
#             node, cost = graph[y][x]
#             # 증가분만큼 증가시키고 인접리스트 재할당
#             graph[y][x] = (node, cost + increase)
#     # 다익스트라 함수를 k번 호출
#     dijkstra(start)