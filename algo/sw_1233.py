for t in range(1, 11):
    N = int(input())
    a = N // 2
    ret = 1
    cal = ['+', '-', '*', '/']
    for i in range(N):
        arr = input().split()
        node = int(arr[0])
        value = arr[1]
        if(node <= a):
            if value not in cal: ret = 0
        else:
            if value in cal: ret = 0
    print(f'#{t} {ret}')