T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    # 새로운 result 리스트에 arr 최대값, 최솟값을 순서대로 넣은 후, arr에 최대값, 최솟값을 제거한다.
    # 한 번 반복할 때 최대, 최소값을 모두 넣기 때문에 N/2만큼만 반복한다.
    for i in range(N//2):
        result.append(max(arr))
        result.append(min(arr))
        arr.pop(arr.index(max(arr)))
        arr.pop(arr.index(min(arr)))
    print(f'#{t}', end=' ')
    for i in range(10):
        print(result[i], end=' ')
    print()