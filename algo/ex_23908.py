'''
슬라이딩 윈도우 왜 쓰냐?
=> 훨씬 효율적이라서(빨라서)
O(N)
'''
arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
max_index = 0
max_sum = sum(arr[:5])
sum_v = sum(arr[:5])
for i in range(len(arr)-5):
    sum_v -= arr[i]
    sum_v += arr[i+5]
    if sum_v > max_sum:
        max_sum = sum_v
        max_index = i+1
print(max_index)

# 강사님 코드
# arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
#
# sum_v = sum(arr[:5]) # 처음 윈도우 계산
# max_v = sum_v
# max_idx = 0
# # 공식 for i in range(arr갯수(11개) - 윈도우의연속구간(5개))
#
# for i in range(11-5):
#     # 1. 다음 윈도우 계산
#     sum_v -= arr[i] # 현재 윈도우의 첫번째 element 제거
#     sum_v += arr[i + 5] # 다음 윈도우의 마지막 element 추가
#     # 2. 최대값 갱신
#     if sum_v > max_v:
#         max_v = sum_v
#         # 현재 윈도우 index는 i, 다음 윈도우의 index는 i + 1
#         max_idx = i + 1
#
# print(max_idx)