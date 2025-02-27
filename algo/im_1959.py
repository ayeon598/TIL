T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M: A, B = B, A
    max_result = float('-inf')
    for i in range(abs(N-M)+1): # 두 숫자열 길이 차이만큼 반복
        result = 0
        for j in range(len(A)): # 두 숫자열을 곱한 값의 합을 저장
            result += A[j] * B[i+j]
        if result > max_result: max_result = result # 최댓값 저장
    print(f'#{t} {max_result}')