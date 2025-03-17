# # 방법 1. 배열에서 최솟값을 찾아서 인덱스가 안 겹치는 경우에 더하기
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     row = []
#     column = []
#     num = 0
#     while len(row) < N:
#         min_value = min(map(min, arr))
#         for i in range(N):
#             for j in range(N):
#                 if arr[i][j] == min_value:
#                     if (i not in row) and (j not in column):
#                         row.append(i)
#                         column.append(j)
#                         print(min_value)
#                         num += min_value
#                     else:
#                         arr[i][j] = 10
#                         continue
#         if len(row) == N: break
#     print(f'#{t} {num}')

# 방법 2. 각 행에서 최솟값을 찾아서 안 겹치는 열로 더하고,
#        각 열에서 최솟값을 찾아서 안 겹치는 행으로 더해서 둘 중에 더 작은 값 반환
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_reverse = zip(*arr)
    index = []
    sum_min = 0
    min_arr = []
    min_rev = float('inf')
    for i in arr:
        min_arr.append(min(i))
    a = min(min_arr)
    a_index = arr[min_arr.index(a)].index(a)
    index.append(min_arr.index(a), a_index)
    