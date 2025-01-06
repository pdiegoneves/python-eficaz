# Saiba como fatiar sequências
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle two:', a[3:-3])
print('Reverse:', a[::-1])

assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]