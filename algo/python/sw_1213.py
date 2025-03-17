for t in range(1, 11):
    test_case = int(input())
#     N = input()
#     string = input()
#     print(f'#{test_case} {string.count(N)}')

    N = list(input())
    string = list(input())
    cnt = 0
    for i in range(len(string)):
        index = 0
        while string[i+index] == N[index]:
            index += 1
            if index == len(N):
                cnt += 1
                break
            if i + index >= len(string): break
    print(f'#{test_case} {cnt}')