T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    answer = list(map(int, input().split()))
    a = 1
    b = 0
    sum_score = []
    for i in range(n):
        score = list(map(int, input().split()))
        for j in range(m):
            if score[j] == answer[j]:
                b += a
                a += 1
            else:
                a = 1
        sum_score.append(b)
        b = 0
        a = 1
        score = []
    sum_score.sort()
    result = sum_score[-1] - sum_score[0]
    print(f'#{test_case} {result}')