arr = ['A', 'B', 'C', 'D', 'E']
path = []

n = 3

def dfs(lev, start):
    if lev == n:
        print(path)
        return

    for i in range(start, 5):
        path.append(arr[i])
        dfs(lev+1, i+1)
        path.pop()

dfs(0, 0)