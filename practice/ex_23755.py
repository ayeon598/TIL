import heapq

lst = [5, 2, 8, 1, 9, 4]

pq = []
multi_heap = []
for i in lst:
    if i % 2 == 0:
        heapq.heappush(pq, (0, i))
    else:
        heapq.heappush(pq, (1, i))

while pq:
    multi_heap.append(heapq.heappop(pq))

for i in multi_heap:
    print(i[1], end=' ')