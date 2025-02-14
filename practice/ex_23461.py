time = list(map(int, input().split()))
time.sort()
t = 0
j = 3
for i in time:
    t += i * j
    j -= 1
    if j < 0: j = 0
print(t)