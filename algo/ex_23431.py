text = 'B[45]AB[9994]'
a = 0
num = 0
while a != -1:
    a = text.find('[')
    b = text.find(']')
    num += int(text[a+1:b])
    text = text.replace('[', '', 1)
    text = text.replace(']', '', 1)
    a = text.find('[')
print(num)