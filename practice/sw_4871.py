T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for j in line:
        arr[j[0]].append(j[1])
    for i in range(1, V + 1):
        arr[i].sort()
