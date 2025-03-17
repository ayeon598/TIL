text = 'ABCDE'
arr = list(map(str, input().split()))
dat = [0] * 200
for i in range(len(text)):
    dat[ord(text[i])] += 1

for i in range(3):
    if dat[ord(arr[i])] != 0:
        print('O', end=' ')
    else: print('X', end=' ')