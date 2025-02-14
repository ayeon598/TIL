T = int(input())
for t in range(1, T+1):
    N = int(input())
    dat = [0] * 5001
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
        for j in range(A[i], B[i]+1):
            dat[j] += 1
    P = int(input())
    C = [0] * P
    for i in range(P):
        C[i] = int(input())
    print(f'#{t}', end=' ')
    for i in range(P):
        print(dat[C[i]], end=' ')