def op(x, z, y):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '/':
        if y == 0:
            print('Ошибка')
        else:
            return x / y
    elif z == '*':
        return x * y
num1 = float(input('Число: '))
operation = str(input('Операция: '))
num2 = float(input('Число: '))
res = op(num1, operation, num2)
status = True
print('Ответ: ', res)
while status == True:
    a = str(input('Продолжить операцию? '))
    if a == 'Да':
        operation2 = str(input('Операция: '))
        num3 = float(input('Число: '))
        res = op(res, operation2, num3)
        print('Ответ: ', res)
    elif a == 'Нет':
        status = False
print('Итог: ', res)