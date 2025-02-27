# import sys
# sys.setrecursionlimit(10**7)
#
# T = int(input())
#
# def find_road(a, b):
#     result = 0
#     for j in range(4):
#         y = a + dy[j]
#         x = b + dx[j]
#         if y < 0 or x < 0 or y >= N or x >= N: continue
#         if arr[y][x] == 1: continue
#         elif arr[y][x] == 0:
#             if len(stack) == 1:
#                 if stack[-2] != [y, x]:
#                     stack.append([y, x])
#                     find_road(y, x)
#             elif stack[-2] != [y, x]:
#                 stack.append([y, x])
#                 find_road(y, x)
#         elif arr[y][x] == 3:
#             result = 1
#         if a == 1: return
#     return result
#
#
# for t in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     stack = []
#     dy = [0, 0, 1, -1]
#     dx = [1, -1, 0, 0]
#     for i in range(N):
#         if arr[N-1][i] == 2:
#             stack.append([N-1, i])
#             print(find_road(N-1, i))

T = int(input())
for t in range(1, T+1):
    N = int(input())
