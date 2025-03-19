# def find(n):
#     if boss[n] == 0: # 가르키는 보스가 없으면
#         return n # 최종 보스다
#
#     result = find(boss[n]) # 재귀호출
#     boss[n] = result # 경로압축!!!(이 코드를 추가함으로써 더 효율적이게 된다)
#     return result
#
# def union(t1, t2):
#     a = find(t1) # a는 t1의 보스
#     b = find(t2) # b는 t2의 보스
#     if a == b: return # 보스가 같으면 : 탈락
#     boss[b] = a # b의 보스가 a다
#
# T = int(input())
# for t in range(1, T+1):
#     visited = []
#     N, M = map(int, input().split())
#     boss = [0] * (N+1)
#     arr = list(map(int, input().split()))
#     for i in range(0,2*M,2):
#         union(arr[i], arr[i+1])
#         for j in range(1, N+1):
#             if boss[j] == arr[i+1]: boss[j] = boss[arr[i+1]]
#         if arr[i] not in visited: visited.append(arr[i])
#         if arr[i+1] not in visited: visited.append(arr[i+1])
#     cnt = N - len(visited)
#     boss = set(boss)
#     print(f'#{t} {len(boss) - 1 + cnt}')

def find(n):
    if boss[n] == n:  # 자기 자신이 보스면
        return n

    # 경로 압축을 통해 루트 노드를 찾아 저장
    boss[n] = find(boss[n])
    return boss[n]


def union(a, b):
    a_boss = find(a)
    b_boss = find(b)

    if a_boss != b_boss:
        boss[b_boss] = a_boss  # b의 보스를 a의 보스로 변경


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 초기화: 각자 자신이 보스
    boss = [i for i in range(N + 1)]

    arr = list(map(int, input().split()))

    # Union 연산 수행
    for i in range(0, 2 * M, 2):
        union(arr[i], arr[i + 1])

    # 각 학생이 속한 조의 대표(보스)를 찾아 집합에 추가
    groups = set()
    for i in range(1, N + 1):
        groups.add(find(i))

    # 조의 개수 출력
    print(f'#{t} {len(groups)}')