def find(n):
    if boss[n] == 0:
        return n
    result = find(boss[n])
    return result

def union(t1, t2):
    a = find(t1)
    b = find(t2)
    if a == b: return
    boss[b] = a

boss = [0] * 10
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    union(a, b)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print("O")
    else:
        print("X")