arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))
for i in range(3,-1,-1):
    for j in range(3, -1, -1):
        print(arr[i][j], end=' ')
    print()