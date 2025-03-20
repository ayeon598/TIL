def find_set(n):
    if boss[n] == 0: return n # 값이 0이면 최종 보스다
    boss[n] = find_set(boss[n]) # 경로압축, 재귀호출
    return boss[n]

def union_set(t1, t2):
    a = find_set(t1) # t1의 보스는 a
    b = find_set(t2) # t2의 보스는 b
    if a == b: return # 이미 같은 그룹이면 탈락
    boss[b] = a # b가 a밑으로 들어간다

N, M = map(int, input().split())
boss = [0] * (N+1)
gender = list(map(str, input().split()))
arr = []
cnt = 0
result = 0
for _ in range(M):
    u, v, d = map(int, input().split())
    arr.append((d, u, v))
arr.sort()

for i in arr:
    if find_set(i[1]) == find_set(i[2]):
        continue
    if gender[i[1]-1] == gender[i[2]-1]:
        continue
    union_set(i[1], i[2])
    cnt += 1
    result += i[0]
if cnt != N-1: result = -1
print(result)