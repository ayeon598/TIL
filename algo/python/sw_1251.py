def find_set(n):
    if boss[n] == 0: return n # 값이 0이면 최종 보스다
    boss[n] = find_set(boss[n]) # 경로압축, 재귀호출
    return boss[n]

def union_set(t1, t2):
    a = find_set(t1) # t1의 보스는 a
    b = find_set(t2) # t2의 보스는 b
    if a == b: return # 이미 같은 그룹이면 탈락
    boss[b] = a # b가 a밑으로 들어간다

T = int(input())
for t in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    boss = [i for i in range(N+1)]
    arr = []
    result = 0

    for i in range(N):
        for j in range(i+1, N):
            dist = (x[i]-x[j]) ** 2 + (y[i] - y[j]) ** 2
            cost = E * dist
            arr.append((cost, i, j))
    arr.sort()
    for i in arr:
        if find_set(i[1]) == find_set(i[2]):
            continue
        union_set(i[1], i[2])
        result += i[0]
    print(f'E{t} {result}')

# # 강사님 코드1
# # 정확한 Union-Find 자료구조 - boss를 주소값으로 관리한다.(None 으로 초기화)
# # 알고리즘 문제 풀땐 boss를 자기자신으로 초기화하면 편하다
#
# def find_set(n):
#     if boss[n] == n: return n # 최종보스 리턴
#     result = find_set(boss[n]) # 재귀호출
#     boss[n] = result # 경로압축
#     return result
#
# def union_set(t1, t2):
#     a = find_set(t1)
#     b = find_set(t2)
#     if a == b: return
#     boss[b] = a # t2의 보스가 t1의 보스 밑으로 들어간다
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input()) # 섬의 개수
#     x = list(map(int, input().split()))
#     y = list(map(int, input().split()))
#     E = float(input()) # 세율
#     boss = [i for i in range(N)]
#     members = []
#     cnt = 0
#     sum_v = 0
#     # 구현1. 비용을 기준으로 오름차순 정렬
#     # 섬1, 섬2 계산 || 섬2, 섬1 계산 ---> 그래서 i+1부터
#     for i in range(N):
#         for j in range(i + 1, N):
#             # 좌표배열은 0부터 시작
#             dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
#             cost = dist * E
#             members.append((cost, i, j))
#     members.sort()
#     # 구현2. 다른 그룹이면 그룹 맺기
#     for cost, a, b in members:
#         if find_set(a) == find_set(b): continue
#         union_set(a, b)
#         cnt += 1
#         sum_v += cost
#
#     print(f'#{tc} {round(sum_v)}')

# # 강사님 코드2
# def find_set(n):
#     if boss[n] == None: return n # 최종보스 리턴
#     result = find_set(boss[n]) # 재귀호출
#     boss[n] = result # 경로압축
#     return result
#
# def union_set(t1, t2):
#     a = find_set(t1)
#     b = find_set(t2)
#     if a == b: return
#     boss[b] = a # t2의 보스가 t1의 보스 밑으로 들어간다
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input()) # 섬의 개수
#     x = list(map(int, input().split()))
#     y = list(map(int, input().split()))
#     E = float(input()) # 세율
#     # 0번 노드 비워두고 1번부터
#     boss = [None] * (N + 1)
#     members = []
#     cnt = 0
#     sum_v = 0
#     # 구현1. 비용을 기준으로 오름차순 정렬
#     # 노드번호를 1번부터 시작하게
#     # 섬1, 섬2 계산 || 섬2, 섬1 계산 ---> 그래서 i+1부터
#     for i in range(1, N+1):
#         for j in range(i + 1, N + 1):
#             # 좌표배열은 0부터 시작
#             dist = (x[i-1] - x[j-1]) ** 2 + (y[i-1] - y[j-1]) ** 2
#             cost = dist * E
#             members.append((cost, i, j))
#     members.sort()
#     # 구현2. 다른 그룹이면 그룹 맺기
#     for cost, a, b in members:
#         if find_set(a) == find_set(b): continue
#         union_set(a, b)
#         cnt += 1
#         sum_v += cost
#
#     print(f'#{tc} {round(sum_v)}')