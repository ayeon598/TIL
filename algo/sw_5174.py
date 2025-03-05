T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    par = [0] * (E+2)

