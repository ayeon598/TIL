# T = int(input())
# for t in range(1, T+1):
#     N = float(input())
#     ret = ''
#     k = 1
#     while N != 0:
#         if N - (0.5)**k < 0:
#             ret += '0'
#             k += 1
#         elif N - (0.5)**k == 0:
#             N -= (0.5) ** k
#             ret += '1'
#             break
#         else:
#             N -= (0.5)**k
#             ret += '1'
#             k += 1
#         if len(ret) >= 13:
#             print((f'#{t} overflow'))
#             break
#     if len(ret) < 12: print((f'#{t} {ret}'))

def change(n):
    binary = ''
    power = -1 # 제곱수 (2**-1 부터 시작)
    cnt = 0

    while n > 0 and cnt <= 12:  # n이 0되면 끝, cnt가 13이상되면 overflow
        value = 2 ** power  # (2 ** -1 == 0.1, 2 ** -2 == 0.01 ...)
        if n >= value:  # 뺄 수 있다면
            binary += '1'
            n -= value  # 값을 빼줌
        else:
            binary += '0'

        power -= 1
        cnt += 1
    if n > 0: # value를 다 뺐는데도 n이 남아 있으면 overflow
        return 'overflow'
    else:
        return binary

T = int(input())
for t in range(1, T+1):
    n = float(input())  # 실수 입력
    result = change(n)
    print(f'#{t} {result}')