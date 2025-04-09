def hanoi(n, s, e, m):
    global result
    if n == 1:
        result.append((s, e))
    else:
        hanoi(n-1, s, m, e)
        result.append((s, e))
        hanoi(n-1, m, e, s)

N = int(input())
result = []

hanoi(N, 1, 3, 2)
print(len(result))
for i in range(len(result)):
    print(*result[i])