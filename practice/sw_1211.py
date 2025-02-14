for t in range(1,11):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dat = [0] * 101
    for i in range(100):
        if arr[99][i] != 0: # 맨 밑에 사다리가 있는 경우 찾기
            j = 99
            k = i
            cnt = 0 # 움직인 횟수
            while j > 0:  # j값을 1씩 줄이면서 양 옆을 확인
                if k >= 1 and k <= 98:  # 양 끝이 아닐 경우 양쪽 모두 확인
                    if arr[j][k - 1] == 1:
                        while k - 1 >= 0:
                            if arr[j][k - 1] == 0: break
                            k -= 1
                            cnt += 1
                        j -= 1
                        cnt += 1
                        continue
                    elif arr[j][k + 1] == 1:
                        while k + 1 <= 99:
                            if arr[j][k + 1] == 0: break
                            k += 1
                            cnt += 1
                        j -= 1
                        cnt += 1
                        continue
                elif k == 0:  # 왼쪽 끝일 경우 오른쪽만 확인
                    if arr[j][k + 1] == 1:
                        while k + 1 <= 99:
                            if arr[j][k + 1] == 0: break
                            k += 1
                            cnt += 1
                        j -= 1
                        cnt += 1
                        continue
                elif k == 99:  # 오른쪽 끝일 경우 왼쪽만 확인
                    if arr[j][k - 1] == 1:
                        while k - 1 >= 0:
                            if arr[j][k - 1] == 0: break
                            k -= 1
                            cnt += 1
                        j -= 1
                        cnt += 1
                        continue
                j -= 1
                cnt += 1
                if j == 0: break
            dat[k] = cnt    # dat 배열에 인덱스와 값 할당
            min_num = cnt   # 최솟값을 cnt로 가정
    for i in range(100):
        if dat[i] != 0 and min_num >= dat[i]:
            min_num = dat[i]
            min_index = i
    print(f'#{test_case} {min_index}')