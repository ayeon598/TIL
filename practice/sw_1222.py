for t in range(1, 11):
    N = int(input())
    arr = list(input())
    cal = []
    for i in range(N):
        if arr[i].isdigit():
            cal.append(arr[i])
        else:
            a = cal.pop()
            b = cal.pop()
            cal.append(a+b)
    print(f'#{t} {cal[0]}')