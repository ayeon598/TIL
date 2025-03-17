arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
def get_sum():
    max_sum = float('-inf')
    max_index = 0
    for i in range(len(arr)-4):
        sum_num = 0
        for j in range(i, i+5):
            sum_num += j
        if max_sum < sum_num:
            max_sum = sum_num
            max_index = i
    return max_index

ret = get_sum()
print(ret)