N = int(input())
time_tuples = [tuple(map(int, input().split())) for _ in range(N)]
num = 1
time_tuples.sort(key=lambda time: time[0])
start_temp = time_tuples[0][0]
end_temp = time_tuples[0][1]
for i in range(1, N):
    if time_tuples[i][0] <= end_temp:
        start_temp = time_tuples[i][0]
    else:
        start_temp = time_tuples[i][0]
        end_temp = time_tuples[i][1]
        num += 1
print(num)