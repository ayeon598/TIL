# 이진탐색 기본코드
# def bs(arr, target):
#     start = 0
#     end = len(arr) - 1 # 인덱스는 0부터 시작
#
#     while start <= end:
#         mid = (start + end) // 2
#         # 이진탐색해서 타겟을 찾으면 인덱스를 반환
#         if arr[mid] == target:
#             # return mid
#             return True
#         # 타겟이 중간값 보다 크면 오른쪽 부분 탐색
#         elif arr[mid] < target:
#             start = mid + 1
#         # 타겟이 중간값 보다 작으면 왼쪽 부분 탐색
#         else:
#             end = mid - 1
#
#     return False # 타겟 못찾을 경우
#
# arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# target = 11
# result = bs(arr, target)
# if result: print('찾았다')
# else: print('찾지 못했다')
def bs(arr, target):
    start = 0
    end = len(arr) - 1  # 인덱스는 0부터 시작

    while start <= end:
        mid = (start + end) // 2
        # 이진탐색해서 타겟을 찾으면 인덱스를 반환
        if arr[mid] == target:
            # return mid
            return True
        # 타겟이 중간값 보다 크면 오른쪽 부분 탐색
        elif arr[mid] < target:
            start = mid + 1
        # 타겟이 중간값 보다 작으면 왼쪽 부분 탐색
        else:
            end = mid - 1

    return False # 타겟 못찾을 경우

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arrN = sorted(list(map(int, input().split())))
    arrM = list(map(int, input().split()))


    cnt = 0
    for num in arrM:
        cnt += bs(arrN, num)
    print(f'#{t} {cnt}')