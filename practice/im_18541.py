T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    Sample = list(map(int, input().split()))
    PassCode = list(map(int, input().split()))
    index = 0
    result = [0] * K
    for i in range(N):
        if index >= K: break
        if Sample[i] == PassCode[index]:
            result[index] = Sample[i]
            index += 1
    if result == PassCode: print(f"#{t} 1")
    else: print(f"#{t} 0")