T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    num = 0 # 충전 횟수
    charge = K # 충전되어 있는 양
    dat = [0] * (N+1) # 충전기 위치
    for i in arr:
        dat[i] = 1
    for i in range(1, N):
        charge -= 1
        if charge >= N - i: break   # 충전되어있는 양이 남은 거리보다 많을 때
        elif dat[i] == 1:   # 충전기가 있는 곳에 왔을 때
            a = 0
            for j in range(1, charge+1):    # 지금 갈 수 있는 거리 안에 충전기가 또 있는 경우
                if dat[i+j] == 1: a = 1
            if a == 0:  # 이번에 충전해야 할 때
                charge = K
                num += 1
        if charge == 0: # 충전 못 했을 때
            num = 0
            break
    print(f'#{t} {num}')