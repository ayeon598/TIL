T = int(input())
for t in range(1, T+1):
    N = int(input())
    if N == 10: print(f'#{t} 1')
    else:
        for i in range(1, N//10):
