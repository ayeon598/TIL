T = int(input())
for t in range(1, T+1):
    N = int(input())
    before = list(map(int, input().split()))
    after = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if before[i] != after[i]:   # i번쨰 값이 서로 다를 때
            for j in range (i, N):  # i번째부터 끝까지 값 바꾸기
                if before[j] == 0: before[j] = 1
                else: before[j] = 0
            cnt += 1    # 횟수 증가
        if before == after: break
    print(f'#{t} {cnt}')