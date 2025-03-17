def cal(n):
    if len(arr[n]) == 2: return int(arr[n][1])
    else:
        left = cal(int(arr[n][2]))
        right = cal(int(arr[n][3]))

        if arr[n][1] == '+': return left + right
        elif arr[n][1] == '-': return left - right
        elif arr[n][1] == '*': return left * right
        elif arr[n][1] == '/': return left / right

for t in range(1, 11):
    N = int(input())
    arr = [0] * (N+1)
    for _ in range(N):
        lst = input().split()
        index = int(lst[0])
        arr[index] = lst
    ret = int(cal(1))
    print(f'#{t} {ret}')