def babygin_run(array, cnt):
    for j in range(len(array)-2):
        a, b, c = array[j], array[j+1], array[j+2]
        # if a not in array[:i] and array.count(a) >= 3:
        #     cnt += 1
        if a == b-1 == c-2:
            cnt += 1
    return cnt


def babygin_triplet(array, cnt):
    for k in array:
        if array.count(k) >= 3:
            cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    arr1 = [arr[0], arr[2]]
    arr2 = [arr[1], arr[3]]
    find_gin = False
    for i in range(4, 12, 2):
        arr1.append(arr[i])
        arr2.append(arr[i+1])
        arr1.sort()
        arr2.sort()
        gin1 = babygin_run(arr1, 0) + babygin_triplet(arr1, 0)
        gin2 = babygin_run(arr2, 0) + babygin_triplet(arr2, 0)
        if gin1 == gin2:
            continue
        elif gin1 > gin2:
            print(f'#{t} 1')
            find_gin = True
            break
        elif gin2 > gin1:
            print(f'#{t} 2')
            find_gin = True
            break
    if not find_gin:
        print(f'#{t} 0')