import heapq

lst = [(2, 'BHC'), (1, 'NeNe'), (3, 'KFC'), (1, 'BBQ'), (2, 'Moms'), (4, 'Mc')]

pq = []
multi_heap = []
arr = []

for i in lst:
    heapq.heappush(pq, i)

while len(pq) > 1:
    while pq:
        multi_heap.append(heapq.heappop(pq))
    a = heapq.heappop(multi_heap)
    b = heapq.heappop(multi_heap)
    heapq.heappush(arr, a[1])
    heapq.heappush(arr, b[1])
    c = (a[0]+b[0], heapq.heappop(arr))
    heapq.heappush(multi_heap, c)
    while multi_heap:
        pq.append(heapq.heappop(multi_heap))
    if len(pq) == 1:
        print(pq[0][1], pq[0][0])
        break