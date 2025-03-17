T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input()))
    max_cnt = 0
    for i in range(N-2):
        if arr[i] == 0: continue
        cnt = 1
        for j in range(i+1, N):
            if arr[j] == 1:
                cnt += 1
            if cnt == K:
                if max_cnt < j-i+1:
                    max_cnt = j-i+1
                    break
    print(f'#{t} {max_cnt}')