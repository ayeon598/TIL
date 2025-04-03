def calculate_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def backtrack(current_pos, visited, distance_so_far, positions, house):
    global min_distance

    # 현재까지의 거리가 이미 찾은 최소 거리보다 크면 탐색 중단
    if distance_so_far >= min_distance:
        return

    # 모든 고객을 방문했으면 집까지의 거리를 더해 최소값 갱신
    if len(visited) == len(positions):
        final_distance = distance_so_far + calculate_distance(current_pos, house)
        min_distance = min(min_distance, final_distance)
        return

    # 아직 방문하지 않은 고객들을 방문
    for i in range(len(positions)):
        if i not in visited:
            next_pos = positions[i]
            distance = calculate_distance(current_pos, next_pos)

            visited.add(i)
            backtrack(next_pos, visited, distance_so_far + distance, positions, house)
            visited.remove(i)  # 백트래킹


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    company = (arr[0], arr[1])
    house = (arr[2], arr[3])
    customer = []
    for i in range(4, 4 + 2 * N, 2):
        customer.append((arr[i], arr[i + 1]))

    # 전역 변수로 최소 거리 설정
    min_distance = float('inf')

    # 회사에서 시작하여 백트래킹 실행
    for start_customer in range(N):
        distance_from_company = calculate_distance(company, customer[start_customer])

        # 시작 고객이 너무 멀면 스킵 (가지치기)
        if distance_from_company >= min_distance:
            continue

        visited = set([start_customer])
        backtrack(customer[start_customer], visited, distance_from_company, customer, house)

    print(f'#{t} {min_distance}')