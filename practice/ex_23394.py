범죄자 = [[5, 7, 9, 55], [30, 10, 6, 8]]
아파트주민 = [[1, 2, 3, 4], [5, 7, 10, 15]]
dat = [0] * 100
citizen = 0
criminal = 0
for i in range(2):
    for j in range(4):
        dat[범죄자[i][j]] += 1
for i in range(2):
    for j in range(4):
        if dat[아파트주민[i][j]] == 0:
            citizen += 1
        else: criminal += 1
print(criminal, citizen)