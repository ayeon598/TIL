T = int(input())
# 이진 탐색 함수
def binary_search(target, start, end, cnt):
    if start > end:
        return -1
    mid = (start + end) // 2
    cnt += 1
    if mid == target:
        return cnt
    elif mid > target:
        end = mid
    else:
        start = mid
    return binary_search(target, start, end, cnt)
# 위에서 만든 함수를 이용해서 A,B의 탐색 수를 구함
for t in range(1, T+1):
    P, A, B = map(int, input().split())
    cnt_A = 0   # A의 탐색 수
    cnt_B = 0   # B의 탐색 수
    a = binary_search(A, 1, P, cnt_A)
    b = binary_search(B, 1, P, cnt_B)
    if a < b:
        print(f'#{t} A')
    elif a > b:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')
