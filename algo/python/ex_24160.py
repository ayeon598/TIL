# def dfs(start):
#     global visited
#     global cnt
#     if start == n:
#         print(cnt, end=' ')
#         cnt = 0
#         return
#     visited.append(start)
#     for i in range(4):
#         if i in visited: continue
#         if MAP[start][i] == 0: continue
#         cnt += MAP[start][i]
#         dfs(i)
#
# n = int(input())
# MAP = [
#     [0, 7, 20, 8],
#     [0, 0, 5, 0],
#     [15, 0, 0, 0],
#     [0, 0, 6, 0]
# ]
# cnt = 0
# visited = []
# dfs(0)

n = int(input())
MAP = [
    [0, 7, 20, 8],
    [0, 0, 5, 0],
    [15, 0, 0, 0],
    [0, 0, 6, 0]
]
used = [0] * 4

# 내가 하고싶은건 모든 경로를 탐색(모든 노드 : used기록 안지워주면)
def dfs(now, sum_v):
    if now == n:
        print(sum_v , end = ' ')

    for i in range(4):
        if MAP[now][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        # dfs(i, sum_v + 인접행렬의 좌표) : 재귀호출하면서 가중치를 누적
        dfs(i, sum_v + MAP[now][i])
        used[i] = 0


# 출발점 방문 표시
used[0] = 1
dfs(0, 0)