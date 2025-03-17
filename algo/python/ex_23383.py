arr = [[1, 5, 10, 15],
       [15, 15, 20, 30]]

dat = [0] * 31
idx = 0
for i in range(2):
    for j in range(4):
        idx = arr[i][j]
        dat[idx] += 1

n = int(input())
print(dat[n])