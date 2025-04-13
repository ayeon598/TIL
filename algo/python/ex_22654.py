T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    Q = int(input())
    result = []
    tree = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = (i, j)
            elif arr[i][j] == 'Y':
                end = (i, j)
            elif arr[i][j] == T:
                tree.append((i, j))
    for i in range(Q):
        C, command = input().split()
        C = int(C)


# 강사님 코드
ydir = (-1, 0, 1, 0)
xdir = (0, 1, 0, -1)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[] for _ in range(N)]

    for i in range(N):
        row = input()
        for j in range(N):
            cell = row[j]
            if cell == 'X':
                sy = i
                sx = j
            elif cell == 'Y':
                dy = i
                dx = j
            board[i].append(cell)
    Q = int(input())
    res = []
    for q in range(Q):
        M, cmd = input().split(" ")
        M = int(M)
        y = sy
        x = sx
        dir = 0
        for i in range(M):
            c = cmd[i]
            if c == 'R':
                dir = (dir + 1) % 4
            elif c == 'L':
                dir = dir - 1
                if dir < 0:
                    dir = 3
            elif c == 'A':
                ny = y + ydir[dir]
                nx = x + xdir[dir]
                if ny < 0 or nx < 0 or ny >= N or nx>= N:
                    continue
                if board[ny][nx] == 'T':
                    continue
                y = ny
                x = nx
        if dy == y and dx == x:
            res.append(1)
        else:
            res.append(0)
    print(f"#{tc} ", end = '')
    for r in res:
        print(r, end = ' ')
    print()