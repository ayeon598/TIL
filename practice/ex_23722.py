arr = input().split()
n = len(arr)

def get_count(tar):
    cnt = 0
    for i in range(n):
        # 3(십진수)을 0b11(이진수)
        # tar의 끝짜리가 1인지 판별 True or False
        if tar & 0x1: # 이 연산은 비트연산입니다라는 가독성
            cnt += 1
        tar >>= 1 # 오른쪽으로 한번씩 민다
    return cnt

result = 0
for tar in range(1 << n): # 모든 경우의수 2의 n제곱
    # 0부터 7까지(000, 001, 010, 011, 100, 101, 110, 111)
    if get_count(tar) >= 2:
        result += 1

print(result)