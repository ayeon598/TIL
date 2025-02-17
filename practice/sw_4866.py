T = int(input())
for t in range(1, T+1):
    arr = list(map(str, input()))
    result = []
    for i in arr:   # arr 안에 있는 {, }, (, )를 result list에 추가하기
        if i == '{' or i == '}' or i == '(' or i ==')': result.append(i)
    i = 0
    while i < len(result)-1:    # result를 순회하면서 {}, ()인 경우 두 원소를 제거
        while (result[i] == '{' and result[i+1] == '}') or (result[i] == '(' and result[i+1] == ')'):
            result.pop(i+1)
            result.pop(i)
            if i != 0: i -= 1
            if i == len(result) - 1: break
            if len(result) == 0: break
        i += 1
    if len(result) == 0: print(f'#{t} 1')
    else: print(f'#{t} 0')