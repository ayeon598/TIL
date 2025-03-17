for t in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(N-4):
        a = arr[i+2] - arr[i]
        b = arr[i+2] - arr[i+1]
        c = arr[i+2] - arr[i+3]
        d = arr[i+2] - arr[i+4]
        if a <= 0 or b <= 0 or c <= 0 or d <= 0: continue
        lst = [a, b, c, d]
        cnt += min(lst)
    print(f'#{t} {cnt}')