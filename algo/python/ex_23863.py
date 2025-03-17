# # q 복습
# from collections import deque
# q = deque()
# q.append(5)
# q.append(4)
# q.append(3)
#
# for _ in range(5):
#     num = q.popleft()
#     num = (num*55 + 17) % 11
#     q.append(num)
#
# while q:
#     print(q[0])
#     q.popleft()

# # bfs 트리의 탐색
# from collections import deque
# # 인접 리스트
# alist = [[] for _ in range(7)]
# alist[5] = [3, 1]
# alist[3] = [2]
# alist[1] = [4]
# alist[4] = [0, 6]
#
# q = deque()
# # 항상 q에 start 노드 값을 넣어준다
# q.append(5)
#
# while q:
#     #과정 1번. 큐에서 뺀다(탐색)
#     now = q.popleft()
#     print(now, end= ' ')
#
#     #과정 2번. 다음 갈 곳 예약 걸기(큐 등록)
#     for i in range(len(alist[now])):
#         next = alist[now][i]
#         q.append(next)

# -----------------------------------------------------------------------
'''
문제

'''
# 알고리즘1. 방향배열
# 알고리즘2. BFS(큐, visited 배열)
# BFS의 과정 2가지
# 1. 큐에서 뺀다(탐색)
# 2. 다음 갈 곳 예약 걸기(큐 등록)
# 과정 2번을 실행할 때 조건 3가지
# 조건1. 미로 내부에 있어야 함.
# 조건2. 벽이 아니어야 함.
# 조건3. 최초 방문이어야 함 => 방문을 하면 visited 배열에 방문 기록

# 함수 2개 만들기
# 1번 함수: BFS함수
# 2번 함수: find_start함수(출발점 찾기)

def bfs(y, x):
    q = []
    # visited 배열 초기화
    visited = [[0] * N for _ in range(N)]
    # 시작점을 큐에 등록
    q.append((y, x))
    visited[y][x] = 1 # 시작점 방문 기록
    while q:
        # bfs의 1번과정. 큐에서 뺀다(탐색)
        ty, tx = q.pop(0)
        if arr[ty][tx] == 3:
            return visited[ty][tx]
        # 방향배열 알고리즘
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            k = 1
            if arr[ty][tx] == 4: k = 2  # 점프대인 경우
            ny, nx = ty + dy * k, tx + dx * k
            # bfs의 2번과정. 다음 갈 곳 예약걸기(큐 등록)
            if 0<=ny<N and 0<=nx<N and arr[ny][nx] != 1 and visited[ny][nx]==0:
                q.append((ny, nx))
                # 최초 방문일 경우 방문하고, 방문 기록
                visited[ny][nx] = visited[ty][tx] + 1
    return -1

def find_start(): # 출발점 찾기
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                return y, x # 튜플 형태로 return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sty, stx = find_start()
    ret = bfs(sty, stx)
    print(f'#{t} {ret}')