T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    result = []
    if N % 2 == 0:  # N이 짝수일 때
        first = arr[:N//2]
        second = arr[N//2:]
    else:   # N이 홀수일 때
        first = arr[:N//2+1]
        second = arr[N//2+1:]
    print(f'#{t}', end=' ')
    for i in range(len(first)): # 하나씩 출력
        print(first[i], end=' ')
        if i >= len(second): continue
        print(second[i], end=' ')
    print()