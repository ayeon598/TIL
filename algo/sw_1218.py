for t in range(1, 11):
    N = int(input())
    arr = list(map(str, input()))
    i = 0
    while len(arr) > 1:
        # () or [] or {} or <>인 경우 두 요소를 제거
        if (arr[i] == '(' and arr[i+1] == ')') or (arr[i] == '[' and arr[i+1] == ']') or (arr[i] == '{' and arr[i+1] == '}') or (arr[i] == '<' and arr[i+1] == '>'):
            arr.pop(i+1)
            arr.pop(i)
            if i == 0: continue
            i -= 1
        else: i += 1
        if i >= len(arr) - 1: break
    if len(arr) == 0: print(f'#{t} 1')
    else: print(f'#{t} 0')