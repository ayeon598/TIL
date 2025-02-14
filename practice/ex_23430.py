arr = ['ABCQ', 'B[4]R', 'CCDA', 'BT[15]']

def get_find(text):
    a = text.find('[')
    b = text.find(']')
    if a != -1:
        return text[a+1:b]
    else: return ''

for i in arr:
    s = get_find(i)
    if s != '':
        print(s, end=' ')
