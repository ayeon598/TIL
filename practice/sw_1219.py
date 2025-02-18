for _ in range(10):
    t, N = map(int, input().split())
    arr = [[] for _ in range(100)]
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        arr[lst[i]].append(lst[i+1])
    start = 0
    end = 99
    n = 0
    while start != end:
