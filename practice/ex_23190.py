arr = []
# 직접 순회하여 i 채우기
for i in range(10, -3, -3):
    arr.append(i)
print(*arr)

# 임시변수 t 채우기
# t = 10
# for i in range(5):
#     arr.append(t)
#     t -= 3
# print(*arr)