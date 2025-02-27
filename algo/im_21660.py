T = int(input())
for t in range(1, T+1):
    # n, m1, m2 = map(int, input().split())
    # block = list(map(int, input().split()))
    # block.sort(reverse=True)

    # 런타임 에러: 4/10 - 해결!
    # 이전 코드 : list(block[i] for i in range(0, m1+1, 2))
    # 고친 코드 : list(block[i] for i in range(0, m1*2, 2))
    n, m1, m2 = map(int, input().split())
    block = list(map(int, input().split()))
    block.sort(reverse=True)
    if m1 <= m2:
        block_m1 = list(block[i] for i in range(0, m1*2, 2))
        block_m2 = list(i for i in block if i not in block_m1)
    else:
        block_m2= list(block[i] for i in range(0, m2*2, 2))
        block_m1 = list(i for i in block if i not in block_m2)
    for i in range(m1):
        block_m1[i] *= (i+1)
    for i in range(m2):
        block_m2[i] *= (i+1)
    result = sum(block_m1) + sum(block_m2)
    print(f'#{t} {result}')

    # 런타임 에러: 8/10 - 해결!
    # 이전 코드 : list(block[i] for i in range(0, m1+1, 2))
    # 고친 코드 : list(block[i] for i in range(0, m1*2, 2))
    # n, m1, m2 = map(int, input().split())
    # block = list(map(int, input().split()))
    # block.sort(reverse=True)
    # block_m1 = []
    # block_m2 = []
    # if m1 < m2:
    #     for i in range(0, m1*2, 2):
    #         block_m1.append(block[i])
    #         block_m2.append(block[i+1])
    #     for i in range(2*m1, n):
    #         block_m2.append(block[i])
    # elif m1 == m2:
    #     for i in range(0, n, 2):
    #         block_m1.append(block[i])
    #         block_m2.append(block[i + 1])
    # else:
    #     for i in range(0, m2*2, 2):
    #         block_m1.append(block[i])
    #         block_m2.append(block[i + 1])
    #     for i in range(2*m2, n):
    #         block_m1.append(block[i])
    # for i in range(m1):
    #     block_m1[i] *= (i+1)
    # for i in range(m2):
    #     block_m2[i] *= (i+1)
    # result = sum(block_m1)+sum(block_m2)
    # print(f'#{t} {result}')

    #재익님 코드
    # T_input = int(input())
    #
    # for T in range(1, T_input + 1):
    #     n, m1, m2 = map(int, input().split())
    #     arr = list(map(int, input().split()))
    #
    #     arr.sort(reverse=True)
    #
    #     rank_list = list(range(1, m1 + 1)) + list(range(1, m2 + 1))
    #     rank_list.sort()
    #
    #     price_total = 0
    #
    #     for i in range(n):
    #         price_total += arr[i] * rank_list[i]
    #
    #     print(f"#{T} {price_total}")
