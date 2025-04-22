def dp():
    for i in range(2, N+1):
        dat[i] = dat[i-1] + 1
        if i % 3 == 0:
            dat[i] = min(dat[i], dat[i//3]+1)
        if i % 2 == 0:
            dat[i] = min(dat[i], dat[i//2]+1)
N = int(input())
dat = [0] * (N+1)
dp()
print(dat[N])
cnt = dat[N]
lst = [N]
while cnt > 0:
    cnt -= 1
    print(lst[0], end=' ')
    a = lst.pop(0)
    if a % 3 == 0 and dat[a//3] == cnt:
        lst.append(a//3)
    elif a % 2 == 0 and dat[a//2] == cnt:
        lst.append(a//2)
    else: lst.append(a-1)
print(1)