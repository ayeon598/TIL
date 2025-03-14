T = int(input())
for t in  range(1, T+1):
    A, B, C = map(int, input().split())
    cnt = 0
    while B >= C:
        B -= 1
        cnt += 1
        if B == 0:
            cnt = -1
            break
    while A >= B:
        if cnt == -1: break
        A -= 1
        cnt += 1
        if A == 0:
            cnt = -1
            break
    print(f'#{t} {cnt}')