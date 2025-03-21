# # 방향 배열 + 다익스트라(비용)
# # 인접행렬
# # result배열을 n x n 행렬
# # result = [[float('inf')] * n for _ in range(n)]
# # result[0][0] = 0
#
# # 노드 -> 좌표
# # start값 (비용, (y좌표, x좌표))
# pq = [(0, (0, 0))]
# # 예약걸기
# heapq.heappush(pq, (price_sum, (ny, nx)))
# # 방향배열
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
# for i in range(4):
#     ny, nx = y + dy[i], x + dx[i]
#     if ny < 0 or ny >= n or nx < 0 or nx >= n: continue # 범위 밖이면 countinue
#     next_price = MAP[ny][nx]
#     price_sum = price + next_price
#     # result값보다 더적은 비용 발견하면 ---> 갱신

import heapq

def dijkstra(start):
    n = len(MAP) # 노드의 수 6개
    result = [float('inf')] * n
    result[start] = 0 # 시작 노드
    # 우선순위 큐 초기화
    pq = [(0, start)] # 비용, 노드

    while pq:
        # 1. 힙에서 뺀다(탐색)
        price, now = heapq.heappop(pq)

        if result[now] < price: continue # 다익스트라 전략 1. 더 큰값이 나오면 continue

        # 2. 다음 갈곳 예약 걸기(힙 등록)
        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i] # 다음 노드까지 비용
            price_sum = price + next_price
            if result[i] > price_sum:
                result[i] = price_sum # 다익스트라 전략 2. 더 작은값 나오면 갱신
                heapq.heappush(pq, (price_sum, i)) # (비용, 노드)

    return result

T = int(input())
for t in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]

# # 강사님 코드
# import heapq
#
# def dijkstra(start):
#     n = len(MAP)
#     # result배열을 2차원 배열로 초기화
#     result = [[float('inf')] * n for _ in range(n)]
#     # 시작노드 초기화
#     result[0][0] = 0
#     # (비용, 노드) -> (비용, 좌표)
#     pq =[(0, start)]
#
#     while pq:
#         # 1. 힙에서 뺀다(탐색)
#         price, now = heapq.heappop(pq)
#         y, x = now
#         # 다익스트라 구현1. result값보다 큰비용이 들어오면 continue
#         if result[y][x] < price: continue
#         dy = [-1, 1, 0, 0]
#         dx = [0, 0, -1, 1]
#         # 2. 다음 갈곳 예약 걸기(힙 등록)
#         for i in range(4):
#             ny, nx = y + dy[i], x + dx[i]
#             if ny < 0 or ny >= n or nx < 0 or nx >= n: continue # 범위 밖이면 continue
#             next_price = MAP[ny][nx]
#             price_sum = price + next_price # 누적합
#             # 다익스트라 구현 2. result값보다 더 작은값 들어오면 갱신
#             if result[ny][nx] > price_sum:
#                 result[ny][nx] = price_sum
#                 heapq.heappush(pq, (price_sum, (ny, nx)))
#
#     return result
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     MAP = [list(map(int, input())) for _ in range(N)]
#     start = (0, 0) # 시작 좌상단
#     result = dijkstra(start)
#     # 끝 우하단
#     print(f'#{tc} {result[N-1][N-1]}')