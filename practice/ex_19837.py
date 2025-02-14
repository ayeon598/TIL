T = int(input())
for t in range(1, T+1):
    arr = list(map(str, input()))
    result = []
    for i in arr:
        if i == '{' or i == '}' or i == '(' or i ==')': result.append(i)
    i = 0
    while i < len(result)-1:
        while (result[i] == '{' and result[i+1] == '}') or (result[i] == '(' and result[i+1] == ')'):
            result.pop(i+1)
            result.pop(i)
            if i != 0: i -= 1
            if i == len(result) - 1: break
            if len(result) == 0: break  # result가 빈 리스트가 되었을 때를 고려하지 않음
        i += 1
    if len(result) == 0: print(f'#{t} 1')
    else: print(f'#{t} 0')