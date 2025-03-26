T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr.pop(0)
    amount = arr[0] # 현재 배터리 용량
    cnt = 0 # 충전 횟수
    num = 1 # 충전한 정류장 번호
    max_amount = 0  # 현재 배터리로 갈 수 있는 정류장 중 가장 큰 충전지 용량
    while num+amount < N:   # 충전한 정류장에서 종점까지 갈 수 있으면 끝
        for i in range(num, num+amount):
            if i >= N-1: break  # i가 arr 길이보다 크면 break
            if max_amount <= arr[i]:
                max_amount = arr[i]
                num = i + 1
        cnt += 1
        amount = max_amount
        max_amount = 0
    print(f'#{t} {cnt}')