node = "12345"
MAP = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

N = int(input())
index = node.index(str(N))
for i in range(5):
    if MAP[index][i] == 0: continue
    print(node[i])