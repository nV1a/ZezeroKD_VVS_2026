def p(x, y):
    return x + y
def m(x, y):
    return x - y
def pr(x, y):
    return x * y
def d(x, y):
    return x/y
x = float(input('Введите число: '))
z = str(input('Введите знак операции: '))
y = float(input('Введите число: '))
if z == '+':
    print(p(x, y))
elif z == '-':
    print(m(x, y))
elif z == '*':
    print(pr(x, y))
elif z == '/':
    print(d(x, y))
else:
    print('Ошибка')
