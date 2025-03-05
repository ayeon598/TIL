T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    length = []
    for i in arr:
        if arr[0] - i != 0: length.append(arr[0] - i)
    if len(length) == 0: day = 0
    else:
        day = 1
        while length.count(0) != len(length):
            if len(length) == 1 and length[0] == 2 and day % 2 == 1:
                day += 1
                continue
            elif len(length) == 1 and length[0] == 1 and day % 2 == 0:
                day += 1
                continue
            if day % 2 == 1:
                length[0] -= 1
                if length[0] == 0: length.pop(0)
                if length.count(0) == len(length): break
                day += 1
            else:
                for j in range(len(length)):
                    if length[j] != 0 and length[j] >= 2:
                        length[j] -= 2
                        if length[j] == 0: length.pop(j)
                        break
                if length.count(0) == len(length): break
                day += 1
    print(f'#{t} {day}')