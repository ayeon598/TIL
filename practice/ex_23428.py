text = 'helloworld[92084]answer'
a = text.find('[')
b = text.find(']')
for i in range(a+1,b):
    print(text[i], end='')