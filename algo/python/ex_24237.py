import heapq

MAP = [[0]*6 for _ in range(6)]
MAP[0][1] = 15
MAP[0][2] = 17
MAP[0][3] = 22
MAP[1][2] = 5
MAP[2][3] = 6
MAP[2][4] = 2
MAP[2][5] = 8
MAP[3][5] = 7
MAP[4][5] = 1

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
# start 0번노드
result = dijkstra(0)
print(*result)