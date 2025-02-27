T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):  # index가 j인 문자부터 M까지의 길이를 반복하므로 범위는 N-M+1까지로 제한
            row = ''
            column = ''
            for k in range(M):
                row += arr[i][j+k]  # 가로로 길이가 M인 문자열 구하기
                column += arr[j+k][i]   # 세로로 길이가 M인 문자열 구하기
            if row == row[::-1]:    # 회문이면 출력
                print(f'#{t} {row}')
                break
            if column == column[::-1]:  # 회문이면 출력
                print(f'#{t} {column}')
                break