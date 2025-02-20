import heapq

n = int(input())
lst = [(9, 'A'), (8, 'B'), (9, 'A'), (10, 'C'), (15, 'A')]

pq = []
multi_heap = []
result = []

for i in lst:
    heapq.heappush(pq, (i[0], -ord(i[1])))

for _ in range(n):
    a = heapq.heappop(pq)
    b = (a[0] * 2) % 17
    heapq.heappush(pq, (b, a[1]))

while pq:
    multi_heap.append(heapq.heappop(pq))

for i in multi_heap:
    print(f'({i[0]}, {chr(-i[1])})', end=' ')
