T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_score = float('-inf')
    min_score = float('inf')
    for i in range(N):
        for j in range(N):
            sum_score = 0
            sum_score += sum(arr[i][k] for k in range(N))   # i행 숫자 합하기
            sum_score += sum(arr[k][j] for k in range(N))   # j열 숫자 합하기
            sum_score -= arr[i][j]  # 자기 자신은 2번 더해져서 1번 빼기
            if max_score < sum_score:
                max_score = sum_score
            if min_score > sum_score:
                min_score = sum_score
    print(f'#{t} {max_score - min_score}')