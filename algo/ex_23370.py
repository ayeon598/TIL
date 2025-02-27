A = [4, 2, 5, 3, 7, 6]
B = [5, 3, 7]
n = int(input())
# 방법1 - flag 처리
# flag = 1
# for i in range(n, n+len(B)):
#     if A[i] != B[i-n]:
#         flag = 0
#         break
#
# if flag: print('O')
# else: print('X')

# 방법2 - is_same() 함수
def is_same(A, B, n):
    flag = 1
    for i in range(n, n + len(B)):
        if A[i] != B[i - n]:
            flag = 0
            break

    if flag:
        print('O')
    else:
        print('X')
is_same(A, B, n)