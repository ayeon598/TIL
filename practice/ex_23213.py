lst = list(map(int, input().split()))
cnt = 0
for i in range(len(lst)):
    if lst[i] == 7:
        cnt += 1
print(cnt)