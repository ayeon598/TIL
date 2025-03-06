n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    left = i
    right = i
    while sum(arr[left:right+1]) <= m:
        if sum(arr[left:right+1]) == m:
            cnt += 1
            break
        elif sum(arr[left:right+1]) < m:
            right += 1
            if right >= n: break
print(cnt)