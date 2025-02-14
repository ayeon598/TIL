def plus(x):
    if x > 5:
        minus(x-1)
    else:
        print(x, end=' ')
        plus(x+1)

def minus(x):
    print(x, end=' ')
    if x-1 >= 0:
        minus(x-1)

x = 0
plus(x)