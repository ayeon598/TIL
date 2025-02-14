A = [5, 2, 5, 7, 3]
n = int(input())
def get_count(n):
    cnt = 0
    for i in range(len(A)):
        if A[i] == n:
            cnt += 1
    print(cnt)
get_count(n)

A = [5, 2, 5, 7, 3]

# 강사님 풀이
# def get_count(n):
#     cnt = 0
#     for i in range(len(A)):
#         if A[i] == n: cnt += 1
#
#     return cnt
#
# n = int(input())
# ret = get_count(n)
# print(ret)