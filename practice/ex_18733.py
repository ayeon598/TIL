N = int(input())
arr = list(map(int, input().split()))
time = 0
for i in range(N-1):
    arr.sort()
    arr.append(arr[0]+arr[1])
    time += arr[0] + arr[1]
    arr.pop(1)
    arr.pop(0)
print(time)