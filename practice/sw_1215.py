for t in range(1, 11):
    N = int(input())
    arr = [tuple(map(str, input())) for _ in range(8)]
    cnt = 0
    for i in range(8-N+1):
        for j in range(8):
            row = []
            column = []
            for k in range(N):
                row.append(arr[i+k][j])
                column.append(arr[j][i+k])
            if row == row[::-1]: cnt += 1
            if column == column[::-1]: cnt += 1
    print(f'#{t} {cnt}')