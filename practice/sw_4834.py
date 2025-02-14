T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = list(map(int, input()))
    arr.sort(reverse=True)  # 크기가 큰 순서로 정렬
    # arr에 있는 모든 값에 대해 count 함수로 중복 값 개수를 세서 리스트 c에 넣기
    c = list(arr.count(arr[i]) for i in range(n))
    # c에서 가장 큰 값이 있는 요소의 인덱스 값 구하기
    max_index = c.index(max(c))
    # 위에서 구한 인덱스로 arr에서 숫자 구하기, max(c)가 1일 때는 arr에서 인덱스0번 값 출력
    if max(c) == 1:
        print(f'#{t} {arr[0]} {max(c)}')
    else:
        print(f'#{t} {arr[max_index]} {max(c)}')
