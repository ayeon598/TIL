T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = list(map(int, input().split()))
    arr = [0] * N
    num = 0
    for i in range(N):
        if arr[i] != result[i]:
            for j in range(i, N, i+1):
                if arr[j] == 0: arr[j] = 1
                else: arr[j] = 0
            num += 1
        if arr == result: break
    print(f'#{t} {num}')