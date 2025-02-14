N = int(input())
# path = []
# cnt = 0
# def dice(x):
#     global cnt
#     if x == N:
#         if sum(path) <= 10:
#             cnt += 1
#             return cnt
#
#     for i in range(6):
#         path.append(i+1)
#         dice(x+1)
#         path.pop()
#
# print(dice(0))

path = []
cnt = 0
def KFC(x):
    global cnt

    # if sum > 10:
    #     return    # 가지치기

    if x == N:
        if sum(path) <= 10:
            cnt += 1
        return

    for i in range(1,7):
        path.append(i)
        KFC(x+1)
        path.pop()
KFC(0)