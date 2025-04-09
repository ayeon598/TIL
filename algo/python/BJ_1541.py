arr = list(input())
num = []
op = []
str1 = ''
plus = -1
minus = float('inf')
for i in arr:
    if i == '-' or i == '+':
        op.append(i)
        if str1 != '':
            num.append(int(str1))
            str1 = ''
    else:
        str1 += i
num.append(int(str1))
for i in op:
    if i == '+':
        plus = num.pop(0)
        plus += num.pop(0)
        num.insert(0, plus)
        plus = -1
    else:
        if minus == float('inf'):
            minus = num.pop(0)
        else:
            minus -= num.pop(0)
if minus != float('inf'):
    minus -= num.pop(0)
    num.insert(0, minus)
print(num[0])