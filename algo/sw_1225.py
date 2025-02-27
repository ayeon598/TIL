for _ in range(10):
    t = int(input())
    arr = list(map(int, input().split()))
    while arr[-1] != 0:
        for i in range(1, 6):
            num = arr.pop(0)
            if num - i <= 0:
                arr.append(0)
                break
            arr.append(num-i)
    print(f"#{t}", *arr)
