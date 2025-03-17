# 분할, 정복, 병합
def merge_sort(arr):
    # 정복
    if len(arr) <= 1:
        return arr
    # 분할
    mid = len(arr) // 2
    # 왼쪽(처음부터 mid까지)
    left = merge_sort(arr[:mid])
    # 오른쪽(mid부터 끝까지)
    right = merge_sort(arr[mid:])
    # 병합 함수 호출
    result = merge(left, right)
    return result


def merge(left, right):
    global cnt
    result = []  # append하고, extend 할거다
    i, j = 0, 0

    if left[-1] > right[-1]: cnt += 1

    # 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # 왼쪽 요소가 작거나 같다
            result.append(left[i])
            # 그 다음 element로 이동
            i += 1
        else:
            # 오른쪽 요소가 작다
            result.append(right[j])
            # 그 다음 element로 이동
            j += 1

    # while문 끝나면(한쪽만 남아있다)남은 배열을 extend
    result.extend(left[i:])
    result.extend(right[j:])

    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    sorted_arr = merge_sort(arr)
    print(f'#{tc} {sorted_arr[N // 2]} {cnt}')