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

# 강사님 코드
def get_calculate(arr):
    stack = []
    for i in arr[:-1]: # 처음부터 마지막 제외하고('.' 제외)
        # 숫자면 스택에 push
        if i.isdecimal():
            stack.append(int(i))
        # 연산자면 pop으로 빼서 연산하고, 다시 스택에 push
        elif i in {'+', '-', '*', '/'}:
            if len(stack) < 2: # 계산하려는데 숫자가 2개 미만
                return 'error'
            b = stack.pop()
            a = stack.pop()
            if i == '+': stack.append(a + b)
            elif i == '-': stack.append(a - b)
            elif i == '*': stack.append(a * b)
            elif i == '/': stack.append(a // b)

    if len(stack) != 1:
        return 'error'

    return stack[0] # 남은 한개의 숫자를 return

T = int(input())
for tc in range(1, T + 1):
    Forth = input().split()
    result = get_calculate(Forth)
    print(f'#{tc} {result}')
