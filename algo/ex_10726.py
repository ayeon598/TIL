def solve():
    tar = M
    for i in range(N):
        if tar & 0x1 == 0:
            return 'OFF'
        tar >>= 1   # N번 반복해서 오른쪽으로 밀면서 M의 1비트가 1인지 확인
    return 'ON'

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{t} {solve()}')