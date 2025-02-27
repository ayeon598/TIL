T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        A = arr[i]
        for j in range(n):
            B = arr[j]
            if B == arr[i-1] or B == arr[i] or B == arr[i+1]:
                break
            elif B == arr[n-1] and
