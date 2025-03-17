n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_index = 0
max_sum = sum(arr[:m])
sum_v = sum(arr[:m])
for i in range(n-m):
    sum_v -= arr[i]
    sum_v += arr[i+m]
    if sum_v > max_sum:
        max_sum = sum_v
        max_index = i+1
print(max_index)