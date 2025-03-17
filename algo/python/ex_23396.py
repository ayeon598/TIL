arr = list(map(int, input().split()))
dat = [0] * 101
for i in range(len(arr)):
    dat[arr[i]] += 1
for i in range(len(dat)):
    for _ in range(dat[i]):
        print(i, end=' ')
