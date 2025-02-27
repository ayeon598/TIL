T = int(input())
for t in range(1, T+1):
    num = int(input())
    arr = list(map(int, input().split()))
    dat = [0] * 101
    max_cnt = 0
    max_index = 0
    for i in range(1000):
        dat[arr[i]] += 1
    for i in range(len(dat)):
        if max_cnt <= dat[i]:
            max_cnt = dat[i]
            max_index = i
    print(f'#{t} {max_index}')