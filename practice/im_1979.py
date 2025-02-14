T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        index = 0
        cnt = 0 # 자리 크기
        while index < N:    # 행에 있는 자리 구하기
            if arr[i][index] == 1:
                while arr[i][index] == 1:
                    cnt += 1
                    index += 1
                    if index >= N: break
                if cnt > 1: result.append(cnt)
                cnt = 0
            else: index +=1
        index = 0
        cnt = 0
        while index < N: # 열에 있는 자리 구하기
            if arr[index][i] == 1:
                while arr[index][i] == 1:
                    cnt += 1
                    index += 1
                    if index >= N: break
                if cnt > 1: result.append(cnt)
                cnt = 0
            else: index +=1

    print(f'#{t} {result.count(K)}')    # 크기가 K인 자리 개수 출력