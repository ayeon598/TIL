N = int(input())
path = []
cnt = 0
def dice(lev, sum):
    global cnt
    if sum > 10:    # 가지치기
        return

    if lev == N:
        if sum <= 10:
            cnt += 1
        return

    for i in range(1, 7):
        path.append(i)
        dice(lev+1, sum+i)
        path.pop()

dice(0, 0)
print(cnt)