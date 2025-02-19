from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기 N, 피자의 개수 M
    cheeses = list(map(int, input().split()))  # 초기 치즈의 양
    # 문제에서는 인덱스를 1부터시작
    pizzas = deque([i + 1, p] for i, p in enumerate(cheeses))
    # N개만큼 피자를 popleft()로 빼서 화덕에 넣어야함
    oven = deque()
    for _ in range(N):
        if pizzas:
            oven.append(pizzas.popleft())

    # 화덕에 피자가 한개 남을때 까지 반복
    while len(oven) > 1:
        now = oven.popleft()  # 맨앞의 피자에서 치즈를 확인
        now[1] //= 2  # 꺼낸 피자의 치즈를 반으로 줄임

        if now[1] == 0:  # 치즈가 모두 녹았다면
            if pizzas:  # 남은 피자가 있다면 화덕에 새 피자를 넣기
                oven.append(pizzas.popleft())
        else:  # 치즈가 남아있다면
            oven.append(now)

    # 남은 피자의 번호 출력        
    print(f'#{tc} {oven[0][0]}')