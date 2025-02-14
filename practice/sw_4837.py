T = int(input())
for t in range(1, T+1):
    A = [i+1 for i in range(12)]
    N, K = map(int, input().split())
    subsets = [[]]
    num = 0
    for i in A: # 전체 부분집합 구하기
        size = len(subsets)
        for j in range(size):
            subsets.append(subsets[j]+[i])
    for subset in subsets:  # 부분집합 합이 K인 개수 구하기
        if len(subset) == N:
            if sum(subset) == K:
                num += 1
    print(f'#{t} {num}')