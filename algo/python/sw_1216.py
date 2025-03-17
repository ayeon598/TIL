for _ in range(10):
    t = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    length = 0
    for i in range(100, 0, -1): # 회문 길이 설정 - 100부터 1씩 줄이면서 확인
        for j in range(100-i+1):
            for k in range(100):
                row = []
                column = []
                for l in range(i):
                    row.append(arr[j + l][k])
                    column.append(arr[k][j + l])
                if row == row[::-1]:    # 회문이 나오면 회문 길이로 i를 할당하고 break
                    length = i
                    break
                if column == column[::-1]:
                    length = i
                    break
            if length != 0: break
        if length != 0: break
    print(f'#{t} {length}')