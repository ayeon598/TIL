# 전위순회
def f_tree(start):
    global f_str
    if start > N: return

    f_str += str(d[start])
    f_tree(start*2)
    f_tree(start*2+1)
# 중위순회
def m_tree(start):
    global m_str
    if start > N: return

    m_tree(start*2)
    m_str += str(d[start])
    m_tree(start*2+1)
# 후위순회
def b_tree(start):
    global b_str
    if start > N: return

    b_tree(start*2)
    b_tree(start*2+1)
    b_str += str(d[start])

N = int(input())
arr = [list(map(int, ord(input().split()))) for _ in range(N)]
d = [0] * 10000
f_str = ''
m_str = ''
b_str = ''
for i in range(N):
    d[arr[i][0]] = [arr[i][1], arr[i][2]]