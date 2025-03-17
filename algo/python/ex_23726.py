N = int(input())
path = []
arr = [1, 2, 3, 4, 5, 6]

def dfs(lev, start):
    if lev == N:
        print(path)
        return

    for i in range(start, 6):
        path.append(arr[i])
        dfs(lev + 1, i)
        path.pop()

dfs(0, 0)