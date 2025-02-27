T = int(input())
for t in range(1, T+10):
    str = input()
    stack = []
    for i in str:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    print(f'#{t} {len(stack)}')