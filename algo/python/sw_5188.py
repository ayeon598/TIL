def find_route(y, x, cnt):
    global min_sum
    if y == N-1 and x == N-1:
        min_sum = min(min_sum, cnt)
    if x < N-1:
        find_route(y, x+1, cnt + arr[y][x+1])
    if y < N-1:
        find_route(y+1, x, cnt + arr[y+1][x])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    find_route(0, 0, arr[0][0])
    print(f'#{t} {min_sum}')


# def dfs(y, x, sum_v):
#     global min_sum
#     # 경로끝에 도달했을때(정점 노드 도달) return
#     if y == N-1 and x == N-1:
#         min_sum = min(min_sum, sum_v)
#
#     # 가지치기(최소합보다 sum_v가 크면 탐색을 할 필요가 없다)
#     if sum_v >= min_sum:
#         return
#
#     # 오른쪽으로 이동
#     if x < N - 1:
#         dfs(y, x+1, sum_v + arr[y][x+1])
#
#     # 아래로 이동:
#     if y < N - 1:
#         dfs(y+1, x, sum_v + arr[y+1][x])
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     min_sum = float('inf')
#     dfs(0, 0, arr[0][0])
#     print(f'#{tc} {min_sum}')