T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        num = arr.pop(0)
        arr.append(num)
    print(f'#{t} {arr[0]}')