N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
len_time = [0] * N
time = []
class_time = []
num = 0
n = 0
for i in arr:
    lst = []
    len_time[n] = i[1] - i[0]
    for j in range(i[0], i[1]):
        lst.append(j)
    time.append(lst)
    n += 1
n = 0
for i in range(N):
    k = len_time.index(min(len_time))
    for j in time[k]:
        if j in class_time:
            n = 1
            break
    if n == 0:
        for j in time[k]:
            class_time.append(j)
        num += 1
    len_time.pop(k)
    time.pop(k)
print(num)