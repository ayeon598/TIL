node = "BTAR"
MAP = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

num = int(input())
for i in range(4):
    # if MAP[num][i] == 1: print(node[i])
    if MAP[num][i] == 0: continue
    print(node[i])