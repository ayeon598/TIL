A = [[5, 5, 2, 6],[9, 1, 1, 3]]
tar = [5, 6, 1, 1, 1, 1, 5, 4]

def get_count():
    for i in range(2):
        for j in range(4):
            print(tar.count(A[i][j]), end=' ')
        print()
get_count()