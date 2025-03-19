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
union(6, 7)
union(5, 6)
union(1, 2)
a, b = map(int, input().split())
if find(a) == find(b): print("O")
else: print("X")