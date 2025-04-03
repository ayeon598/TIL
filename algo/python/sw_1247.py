def cal_distance(a, b):
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return dist


def find_route(now, visited):
    global min_cnt
    global cnt

    if len(visited) == N:
        final_dist = cnt + cal_distance(now, house)
        min_cnt = min(min_cnt, final_dist)
        return

    for j in range(N):
        if j in visited:
            continue

        next_point = customer[j]
        distance = cal_distance(now, next_point)
        cnt += distance
        visited.append(j)
        find_route(next_point, visited)
        visited.pop()
        cnt -= distance


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    company = (arr[0], arr[1])
    house = (arr[2], arr[3])
    customer = []
    min_cnt = float('inf')

    for i in range(4, 4 + 2 * N, 2):
        customer.append((arr[i], arr[i + 1]))

    for i in range(N):
        cnt = cal_distance(company, customer[i])
        find_route(customer[i], [i])

    print(f'#{t} {min_cnt}')