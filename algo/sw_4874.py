T = int(input())
for t in range(1, T+1):
    str = input()
    num = []
    for i in str.split():
        if i.isdigit():
            num.append(int(i))
        elif i == '.':
            if len(num) == 1: print(f'#{t} {num.pop()}')
            else: print(f'#{t} error')
        else:
            if len(num) < 2:
                print(f'#{t} error')
                break
            a = num.pop()
            b = num.pop()
            if i == '+': num.append(int(a+b))
            elif i == '-': num.append(int(b-a))
            elif i == '*': num.append(int(a*b))
            else: num.append(int(b/a))