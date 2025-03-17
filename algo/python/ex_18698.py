money = int(input())
num = 0
i = money
while i > 0:
    if i - 500 > 0:
        num += 1
        i -= 500
    elif i - 100 > 0:
        num += 1
        i -= 100
    elif i - 50 > 0:
        num += 1
        i -= 50
    else:
        num += 1
        i -= 10
print(num)