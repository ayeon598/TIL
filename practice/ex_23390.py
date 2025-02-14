땅 = [[4, 5, 7, 6], [1, 5, 5, 4], [1, 1, 1, 1]]
주민 = [[5, 6, 4], [1, 5, 3]]
dat = [0] * 8
for i in range(3):
    for j in range(4):
        dat[땅[i][j]] += 1
for i in range(2):
    for j in range(3):
        print(dat[주민[i][j]], end=' ')
    print()