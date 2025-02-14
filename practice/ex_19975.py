T = int(input())
for t in range(1, T+1):
    arr = list(map(str, input()))
    i = 0
    while i < len(arr)-1:
        while arr[i] == arr[i+1]:
            arr.pop(i+1)
            arr.pop(i)
            if len(arr) <= 1: break
            if i != 0: i -= 1
            if i == len(arr)-1: break # 마지막 2개를 제거한 후 인덱스를 고려하지 않음
        i += 1
    print(f'#{t} {len(arr)}')