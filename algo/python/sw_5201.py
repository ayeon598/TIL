T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    amount = list(map(int, input().split()))
    sum_amount = 0
    weight.sort(reverse=True)
    amount.sort(reverse=True)
    for j in range(M):
        for i in weight:
            if i <= amount[0]:
                sum_amount += i
                amount.pop(0)
                weight.pop(weight.index(i))
                break
    print(f'#{t} {sum_amount}')