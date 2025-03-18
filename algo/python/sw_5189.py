def used_amount(now, amount, cnt):
    global min_sum
    if cnt == N-1:
        if arr[now][0]:
            amount += arr[now][0]
            min_sum = min(min_sum, amount)
    for i in range(1, N):
        if arr[now][i] == 0 or visited[i] == 1: continue
        visited[i] = 1
        used_amount(i, amount + arr[now][i], cnt + 1)
        visited[i] = 0



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_sum = float('inf')
    visited[0] = 1
    used_amount(0, 0, 0)
    print(f'#{t} {min_sum}')

# def dfs(now, sum_v, cnt):
#     global min_v
#     # 가지치기
#     if sum_v >= min_v:
#         return
#     # min_v를 언제 구할까?
#     # 모든 구역을 방문했을떄
#     if cnt == N-1: # 사무실 제외
#         if MAP[now][0]:# 사무실에 도착하는 경로가 있다면
#             sum_v += MAP[now][0] # 사무실 비용
#             min_v = min(min_v, sum_v)
#
#     for i in range(1, N): #사무실
#         if MAP[now][i] == 0: continue
#         if used[i] == 1: continue
#         used[i] = 1
#         dfs(i, sum_v + MAP[now][i], cnt+1)
#         used[i] = 0
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     MAP = [list(map(int, input().split())) for _ in range(N)]
#     used = [0] * N
#     min_v = float('inf')
#     # 사무실이 출발지 방문처리
#     used[0] = 1
#     dfs(0, 0, 0)
#     print(f'#{tc} {min_v}')