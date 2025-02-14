for t in range(1, 11):
    num_test = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_num = 0
    for i in range(100):
        row = 0
        column = 0
        s1 = 0
        s2 = 0
        for j in range(100):
            row += arr[i][j]
            column += arr[j][i]
            s1 += arr[j][j]
            s2 += arr[j][99-j]
        if max_num < row:
            max_num = row
        if max_num < column:
            max_num = column
        if max_num < s1:
            max_num = s1
        if max_num < s2:
            max_num = s2
    print(f'#{num_test} {max_num}')