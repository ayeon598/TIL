arr = [[1, 2, 1, 3, 1],
       [2, 2, 2, 2, 2],
       [1, 0, 1, 0, 1],
       [3, 1, 2, 1, 3]]

y = 0
x = 1
sum_v = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(4):
       ny = y + dy[i]
       nx = x + dx[i]

       if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
       sum_v += arr[ny][nx]

print(sum_v)
