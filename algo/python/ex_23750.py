import heapq

lst = [5, 2, 8, 1, 9]
pq = []
min_heap = []
for i in lst:
    heapq.heappush(pq, i)

while pq:
    min_heap.append(heapq.heappop(pq))

print(min_heap)