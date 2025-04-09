N = int(input())
arr = [int(input()) for _ in range(N)]
num = 0
sum_num = 0
while len(arr) > 1:
    num = min(arr)
    arr.remove(min(arr))
    num += min(arr)
    arr.remove(min(arr))
    arr.append(num)
    sum_num += num
    if len(arr) == 1: break
print(sum_num)