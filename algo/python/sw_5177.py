T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    for i in range(1, N+1):
        tree[i] = arr[i-1]
        if i == 1: continue
        j = i
        while tree[j] < tree[j//2]:
            tree[j], tree[j//2] = tree[j//2], tree[j]
            j = j // 2
    node = N
    sum_num = 0
    while node > 1:
        node = node // 2
        sum_num += tree[node]
        if node == 1: break
    print(f'#{t} {sum_num}')