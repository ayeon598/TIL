'''
투 포인터 알고리즘: 두 원소의 합이 m
1. left, right 시작값을 어디에 둘지 초기화
    배열 sort
    left: 배열[0], right: 배열[-1]
2-1. left + right < m: left += 1
2-2. else: right -= 1
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = n-1
while arr[left] + arr[right] != m:
    if arr[left] + arr[right] < m:
        left += 1
    else: right -= 1
    if left == right:
        print("찾을 수 없음")
        break
if left != right:
    print(left, right)
