import heapq

lst = [5, 2, 8, 1, 9]

pq = []
max_heap = []

for i in lst:
    heapq.heappush(pq, -i)

while pq:
    max_heap.append(-heapq.heappop(pq))

print(max_heap)