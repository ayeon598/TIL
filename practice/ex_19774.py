T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            row = ''
            column = ''
            for k in range(M):
                row += arr[i][j+k]
                column += arr[j+k][i]
            if row == row[::-1]:
                print(f'#{t} {row}')
                break
            if column == column[::-1]:
                print(f'#{t} {column}')
                break