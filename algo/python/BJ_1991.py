# 전위순회
def f_tree(start):
    if start == '.': return ''
    left, right = tree[start]
    return start + f_tree(left) + f_tree(right)
# 중위순회
def m_tree(start):
    if start == '.': return ''
    left, right = tree[start]
    return m_tree(left) + start + m_tree(right)
# 후위순회
def b_tree(start):
    if start == '.': return ''
    left, right = tree[start]
    return b_tree(left) + b_tree(right) + start

N = int(input())
tree = {}
for _ in range(N):
    p, l, r = input().split()
    tree[p] = (l, r)

print(f_tree('A'))
print(m_tree('A'))
print(b_tree('A'))