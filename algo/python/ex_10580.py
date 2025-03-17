T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in arr:
        start = i[0]
        end = i[1]
        if start == end: continue
        for j in arr:
            if i == j: continue
            if start < j[0] and j[1] < end: cnt += 1
            elif start > j[0] and j[1] > end: cnt += 1
    print(f'#{t} {cnt}')