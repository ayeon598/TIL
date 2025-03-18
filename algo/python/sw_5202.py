T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    time = [0] * 25
    cnt = 0
    possible = True
    for _ in range(N):
        s, e = map(int, input().split())
        arr.append((s, e))
    arr.sort(key=lambda x: x[1] - x[0])
    for i in range(N):
        for j in range(arr[i][0], arr[i][1]):
            if time[j] == 1:
                possible = False
                break
        if possible:
            cnt += 1
            for j in range(arr[i][0], arr[i][1]):
                time[j] = 1
        else: possible = True
    print(f'#{t} {cnt}')