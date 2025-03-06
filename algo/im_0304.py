T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    max_cnt = 0
    for i in range(N):
        left = i
        right = i
        while arr[right] - arr[left] <= K:
            right += 1
            if right >= N: break
        cnt = right - left
        max_cnt = max(max_cnt, cnt)
    print(f'#{t} {max_cnt}')