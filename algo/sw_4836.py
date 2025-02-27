T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    field = [[0] * 10 for _ in range(10)]
    cnt = 0 # 보라색 칸 수
    # 주어진 색칠 영역을 돌면서 격자 값이 0일 때는 색칠하려는 색을 넣어주고, 0이 아닐 때는 이미 다른 색으로 칠해진 경우이므로 cnt의 수를 증가시켜준다.
    for n in range(N):
        for i in range(arr[n][0], arr[n][2]+1):
            for j in range(arr[n][1], arr[n][3]+1):
                if field[i][j] == 0:
                    field[i][j] = arr[n][-1]
                else:
                    field[i][j] = 3
                    cnt += 1
    print(f'#{t} {cnt}')