import heapq

N = int(input())
arr = []
sum_num = 0

for _ in range(N):
    heapq.heappush(arr, int(input()))

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    num = a + b
    sum_num += num
    heapq.heappush(arr, num)

print(sum_num)