import heapq

lst = [(7, 'A'), (9, 'C'), (7, 'C'), (6, 'D'), (5, 'A')]

pq = []
multi_heap = []

for i in lst:
    heapq.heappush(pq, (i[-1], -i[0]))

while pq:
    multi_heap.append(heapq.heappop(pq))

for i in multi_heap:
    print(f'({-i[-1]}, {i[0]})', end= ' ')