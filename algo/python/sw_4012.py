# # 5명중에 3명 뽑는다
# # level = 3, branch = 5
# arr = ['A', 'B', 'C', 'D', 'E']
# path = []
#
# def dfs(lev, start):
#     if lev == 3:
#         print(path)
#         return
#
#     for i in range(start, 5):
#         path.append(arr[i])
#         dfs(lev + 1, i + 1)
#         path.pop()
#
# dfs(0, 0)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

# # 강사님 코드
# # 조합
# # 식재료중에 N//2개를 음식에 배정 : level = N//2
# # 총 식재료의 갯수는 N개 : branch = N
#
# def dfs(lev , start):
#     global min_diff
#
#     if lev == N // 2:
#         # N = 4, A에 2개 B에 2개
#         # A_food = [0, 1]
#         # B_food = [2, 3] # 0과 1을 제외한 나머지 식재료
#         A_food = path[:]
#         B_food = [i for i in range(N) if i not in A_food]
#         # A음식의 맛 계산
#         A_taste = 0
#         for y in A_food:
#             for x in A_food:
#                 if y != x: A_taste += synergy[y][x]
#         # A음식의 맛 계산
#         B_taste = 0
#         for y in B_food:
#             for x in B_food:
#                 if y != x: B_taste += synergy[y][x]
#
#         # B음식의 맛 계산
#         diff = abs(A_taste - B_taste)
#         min_diff = min(min_diff, diff)
#         return
#
#     for i in range(start, N):
#         path.append(i)
#         dfs(lev + 1, i + 1)
#         path.pop()
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     synergy = [list(map(int, input().split())) for _ in range(N)]
#     path = []
#     min_diff = float('inf')
#     dfs(0, 0)
#     print(f'#{tc} {min_diff}')