name = ['Luffy', 'Zoro', 'Sanji']
arr = ['O', 'X']
path = []

def print_name():
    for i in range(3):
        if path[i] == 'O': print(name[i], end=' ')
    print()

def dfs(lev):
    if lev == 3:
        print_name()
        return
    for i in range(2):
        path.append(arr[i])
        dfs(lev + 1)
        path.pop()
dfs(0)