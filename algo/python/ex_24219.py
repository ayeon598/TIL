def find(n):
    if boss[n] == 0: # 가르키는 보스가 없으면
        return n # 최종 보스다

    result = find(boss[n]) # 재귀호출
    boss[n] = result # 경로압축!!!(이 코드를 추가함으로써 더 효율적이게 된다)
    return result

def union(t1, t2):
    a = find(t1) # a는 t1의 보스
    b = find(t2) # b는 t2의 보스
    if a == b: return # 보스가 같으면 : 탈락
    boss[b] = a # b의 보스가 a다

boss = [0] * 100

N = int(input())
visited = []
for _ in range(N):
    a, b = map(ord, input().split())
    union(a, b)
    for i in range(100):
        if boss[i] == b: boss[i] = boss[b]
    if a not in visited: visited.append(a)
    if b not in visited: visited.append(b)

boss = set(boss)
print(len(boss)-1)
print(26-len(visited))

