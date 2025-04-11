T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    Q = int(input())
    result = []
    tree = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = (i, j)
            elif arr[i][j] == 'Y':
                end = (i, j)
            elif arr[i][j] == T:
                tree.append((i, j))
    for i in range(Q):
        C, command = input().split()
        C = int(C)