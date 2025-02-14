N = int(input())
path = []
used = [0] * 6 # 이미 사용한 카드인지 아닌지 구분하는 배열
def dice(x):
    if x == N:
        print(path)
        return

    for i in range(6):
        if used[i] == 1: continue
        used[i] = 1 # 사용했다고 기록
        path.append(i+1)
        dice(x + 1)
        path.pop()
        used[i] = 0 # 사용기록을 pop() 돌아왔을떄 지워줘야한다

dice(0)