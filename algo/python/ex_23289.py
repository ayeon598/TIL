arr = [[1, 2, 1, 3, 1],
       [2, 2, 2, 2, 2],
       [1, 0, 1, 0, 1],
       [3, 1, 2, 1, 3]]
y = 1
x = 2
sum_v = 0
sum_v += arr[y-1][x+0]
sum_v += arr[y+1][x+0]
sum_v += arr[y+0][x-1]
sum_v += arr[y+0][x+1]
print(sum_v)