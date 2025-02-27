text = 'ABCDEFABCKKKKKABC'
a = 0
num = 0
while a != -1:
    a = text.find('ABC')
    if a != -1: num += 1
    text = text.replace('ABC', '', 1)
    a = text.find('ABC')
print(num)