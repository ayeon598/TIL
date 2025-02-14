A = [5, 7, 5, 4, 2, 9]
B = [5, 4, 2, 5, 6]

def is_exist(n):
    for i in range(n):
        if A[i] in B:
            print("O", end=' ')
        else:
            print("X", end=' ')
is_exist(len(A))

# 강사님 풀이
# A = [5, 7, 5, 4, 2, 9]
# B = [5, 4, 2, 5, 6]
#
# def is_exist(n): # 존재하냐?
#     # A를 순회할까? B를 순회할까?
#     # 존재하면 return 1, 존재하지 않으면 return 0
#     for i in range(5):
#         if B[i] == n: return 1
#     return 0
#
# # O나 X를 출력(함수호출하면서)
# for i in range(6):
#     if is_exist(A[i]): print('O', end = ' ')
#     else: print('X', end = ' ')