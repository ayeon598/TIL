# T = int(input())
# for t in range(1, T+1):
#     str1 = list(map(str, input()))
#     str2 = list(map(str, input()))
#     index = 0
#     for i in range(len(str2)):
#         if len(str2) < len(str1): break
#         if str2[i] == str1[index]:
#             while str2[i+index] == str1[index]:
#                 index += 1
#                 if index >= len(str1): break
#                 if i+index > len(str2):
#                     index = 0
#                     break
#             if index < len(str1): index = 0
#         if index >= len(str1): break
#     print(f'#{t}', end=' ')
#     if index >= len(str1): print(1)
#     else: print(0)

T = int(input())
for t in range(1, T+1):
    str1 = str(input())
    str2 = str(input())
    if str2.find(str1) == -1: print(f'#{t} 0')
    else: print(f'#{t} 1')