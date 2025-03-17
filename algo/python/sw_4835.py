T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    min_value = 0
    max_value = 0
    # 첫 번째 값을 최솟값, 최댓값 변수에 할당
    for i in range(m):
        min_value += arr[i]
        max_value += arr[i]
    # index i번째부터 m만큼 더해야하기 때문에 범위를 n-m+1로 정함
    for i in range(n-m+1):
        s = 0
        # 최대, 최솟값 구하기
        for j in range(m):
            s += arr[i+j]
        if min_value > s:
            min_value = s
        if max_value < s:
            max_value = s
    print(f'#{t} {max_value - min_value}')
