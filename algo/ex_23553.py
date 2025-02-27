# def call_i(i):
#     if i >= 7: return
#     j = 1
#     call_j(i, j)
#     call_i(i+1)
#
# def call_j(i, j):
#     if j >= 7: return
#     k = 1
#     call_k(i, j, k)
#     call_j(i, j+1)
#
# def call_k(i, j, k):
#     if k >= 7: return
#     print([i, j, k])
#     call_k(i, j, k+1)
#
# call_i(1)

path = []

def KFC(x):
    if x == 3:
        print(path)
        return

    for i in range(1,7):
        path.append(i)
        KFC(x+1)
        path.pop()
KFC(0)