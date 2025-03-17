# level 3, branch 2

def KFC(lev):
    if lev == 3:
        return

    for i in range(2):
        KFC(lev+1)
    print(lev)

KFC(0)