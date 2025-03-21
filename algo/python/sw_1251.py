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