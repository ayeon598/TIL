arr = [list(map(int, input().split())) for _ in range(5)]
c = 0
min_value = arr[0][0]
max_value = arr[0][0]
s = 0
for i in range(5):
    c += arr[i].count(2)
    for j in range(5):
        if min_value > arr[i][j]:
            min_value = arr[i][j]
        if max_value < arr[i][j]:
            max_value = arr[i][j]
        if i == j:
            s += arr[i][j]
print(c)
print(max_value, min_value)
print(s)
