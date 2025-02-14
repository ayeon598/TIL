T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        for k in range(1, j+1):
            if i-1-k >= 0 and i-1+k < N: # 두 값의 인덱스가 모두 N에 포함될 때
                if arr[i-1-k] == arr[i-1+k]:
                    if arr[i-1-k] == 0:
                        arr[i-1-k] = 1
                        arr[i-1+k] = 1
                    else:
                        arr[i-1-k] = 0
                        arr[i-1+k] = 0
            else: break
    print(f'#{t}', *arr)