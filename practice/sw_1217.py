def multi(n, m):    # 함수 한 번 돌 때 sum에 n을 한 번 곱함
    global sum
    if m > 1:
        sum *= n
        multi(n, m-1)
    return sum

for _ in range(10):
    t = int(input())
    N, M = map(int, input().split())
    sum = N
    result = multi(N, M)
    print(f'#{t} {result}')