# T = int(input())
# for t in range(1,T+1):
#     N, C = map(str, input().split())
#     ArrN = [i for i in N]
#     Ans = set(ArrN)
#     Ans = sorted(Ans)
#     max_num = [i for i, value in enumerate(ArrN) if value == Ans[-1]]
#     min_num = [i for i, value in enumerate(ArrN) if value == Ans[0]]
#     for i in range(int(C)):
#         if len(max_num) == 0:
#             Ans.pop(-1)
#             max_num = [i for i, value in enumerate(ArrN) if value == Ans[-1]]
#         if len(min_num) == 0:
#             Ans.pop(0)
#             min_num = [i for i, value in enumerate(ArrN) if value == Ans[0]]
#         if int(C) == 1:
#             ArrN[0], ArrN[max_num[-1]] = ArrN[max_num[-1]], ArrN[0]
#         elif len(max_num) >= 2:
#             ArrN[min_num[0]], ArrN[max_num[-1]] = ArrN[max_num[-1]], ArrN[min_num[0]]
#             min_num.pop(0)
#             max_num.pop(-1)
#         else:
#             ArrN[0], ArrN[max_num[-1]] = ArrN[max_num[-1]], ArrN[0]
#             max_num.pop(-1)
#
#     print(f'#{t}', ''.join(ArrN))

def find_max_num(numbers, change, current_count, visited):
    if visited is None:
        visited = set()

    if current_count == change:
        return int(''.join(map(str, numbers)))

    state = (''.join(map(str, numbers)), current_count)
    if state in visited:
        return 0
    visited.add(state)
    max_prize = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            max_prize = max(max_prize, find_max_num(numbers, change, current_count + 1, visited))
            numbers[i], numbers[j] = numbers[j], numbers[i]

    return max_prize


T = int(input())
for t in range(1, T + 1):
    N, C = map(str, input().split())
    C = int(C)
    ArrN = [int(i) for i in N]

    result = find_max_num(ArrN, C, 0, None)
    print(f'#{t} {result}')
