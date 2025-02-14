n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l = 100
num = 0
for i in arr:
    if l - i >= 0:
        l -= i
        num += 1
    else: break
print(num)