T = int(input())

def divide_arr(dat):
    if len(dat) == 1:
        stack.append(dat[0])
        return
    elif len(dat) == 2:
        if arr[dat[0]] == 3 and arr[dat[1]] == 1:
            stack.append(dat[1])
            return
        elif (arr[dat[0]] == 1 and arr[dat[1]] == 3) or arr[dat[0]] >= arr[dat[1]]:
            stack.append(dat[0])
            return
        else:
            stack.append(dat[1])
            return

    mid = len(dat) // 2
    left = dat[:mid]
    right = dat[mid:]
    divide_arr(left)
    divide_arr(right)

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dat = [i for i in range(N)]
    while len(dat) > 1:
        stack = []
        divide_arr(dat)
        dat = stack
        if len(dat) == 1: break
    print(f'#{t} {dat[0]+1}')