T = int(input())
for t in range(1, T+1):
    str1 = list(map(str, input()))
    str2 = str(input())
    cnt = 0
    for i in str1:  # str1 리스트를 순회하면서 각 문자가 몇 개 있는지 세기
        num = str2.count(i)
        if cnt < num: cnt = num
    print(f'#{t} {cnt}')