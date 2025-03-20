import heapq

def dijkstra(start):
    n = len(MAP)
    result = [float('inf')] * n
    pq = [(0, start)]

    while pq:
        price, now = heapq.heappop(pq)
        if result[now] < price: continue

        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i]
            price_sum = price + next_price
            if result[i] > price_sum:
                result[i] = price_sum
                heapq.heappush(pq, (price_sum, i))
    return result

MAP = [[0]*6 for _ in range(6)]
MAP[0][1] = 5
MAP[0][2] = 10
MAP[0][3] = 7
MAP[0][5] = 12
MAP[1][0] = 5
MAP[1][5] = 9
MAP[2][5] = 1
MAP[3][2] = 2
MAP[3][4] = 1
MAP[4][5] = 3

s, e = map(str, input().split())
s = ord(s) - ord('A')
e = ord(e) - ord('A')

result = dijkstra(s)
print(result[e])