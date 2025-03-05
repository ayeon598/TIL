T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    node = [[0] * (E+2) for _ in range(E+2)]
    lst = [N]
    k = 0
    for i in range(E):
        node[arr[2*i]][arr[2*i+1]] = 1
    while True:
        for i in range(E+2):
            if node[lst[k]][i] == 1:
                lst.append(i)
        k += 1
        if k >= len(lst): break
    print(f'#{t} {len(lst)}')
