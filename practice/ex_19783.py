def sum_num(s, a, b, num):
    if a != -1:
        num += int(s[a+1:b])
        s = s.replace('[', '', 1)
        s = s.replace(']', '', 1)
    return s, num
def muti_num(s, c, d, num):
    if c != -1:
        num *= int(s[c+1:d])
        s = s.replace('{', '', 1)
        s = s.replace('}', '', 1)
    return s, num
s = str(input())
a = 0
c = 0
num = 0
while a != -1 or c != -1:
    a = s.find('[')
    b = s.find(']')
    c = s.find('{')
    d = s.find('}')
    if (a != -1 and a < c) or c == -1:
        s, num = sum_num(s, a, b, num)
    if (c != -1 and a > c) or a == -1:
        s, num = muti_num(s, c, d, num)
    a = s.find('[')
    c = s.find('{')
print(num)