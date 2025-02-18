lst = ['Luffy', 'Zoro', 'Sanji']
arr = ['O', 'X']
path = []

def dfs(lev):
    if lev == 3:

        return
    for i in range(3):
        path.append(lst[i])
        dfs(lev + 1)
        path.pop()
dfs(0)