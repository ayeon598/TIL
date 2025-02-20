import heapq

n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    for j in range(1, arr[i]+1):
        if j == 1: result = 1
