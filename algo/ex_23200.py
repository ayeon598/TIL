lst = ['A', 'B', 'Q', 'T']
for i in range(len(lst)):
    for j in range(len(lst)-1, -1, -1):
        print(lst[j], end='')
    print()