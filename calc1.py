x = float(input('Введите число: '))
y = float(input('Введите число: '))
z = str(input('+ или - или * или /: '))
res = 0
if z == '+':
    res = x + y
elif z == '-':
    res = x - y
elif z == '*':
    res = x * y
elif z == '/':
    res = x/y
else:
    print('Ошибка')
print(res)