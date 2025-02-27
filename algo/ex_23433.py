text = ['GOLDABCGOLD', 'HELLOWORLD', 'WHITEGOLD']
num = 0
for i in text:
    a = 0
    while a != -1:
        a = i.find('GOLD')
        if a != -1: num += 1
        i = i.replace('GOLD', '', 1)
        a = i.find('GOLD')
print(num)