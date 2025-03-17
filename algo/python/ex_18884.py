import heapq

N = int(input())
arr = [500]
for i in range(N):
    pq = []
    min_heap = []
    a, b = map(int, input().split())
    arr.append(a)
    arr.append(b)
    for j in arr:
        heapq.heappush(pq, j)
    while pq:
        min_heap.append(heapq.heappop(pq))
    print(min_heap[len(min_heap)//2])