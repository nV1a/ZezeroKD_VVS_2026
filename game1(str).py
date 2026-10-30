def lvl1():
    print('Метод str.upper() вернет копию строки str с символами, преобразованными в верхний регистр.')
    print('Метод str.lower() вернет копию строки str, в которой все символы будут преобразованы в нижний регистр.')
    print('Метод str.capitalize() вернет копию строки str с первым символом в верхнем регистре, а остальные символы будут в нижнем регистре.')
    print('Тест:')
    test1 = 'hELLO WORLD'
    print(test1 + '.upper() = ' + test1.upper())
    print(test1 + '.lower() = ' + test1.lower())
    print(test1 + '.capitalize() = ' + test1.capitalize())
    print()
    print('Введите строку: ')
    tx1 = input()
    print('Для выхода выберите 4')
    print('Выберите метод: ')
    ch = int(input())
    if ch == 1:
        print(tx1.upper())
    elif ch == 2:
        print(tx1.lower())
    elif ch == 3:
        print(tx1.capitalize())
    elif ch == 4:
        print('Уровень завершен!')
        return 1
    else:
        print('Нет такого метода')
    return 0


def lvl2():
    print('Метод str.find() возвращает индекс первого совпадения подстроки sub в строке str, где подстрока или символ sub находится в пределах среза str[start:end]. Другими словами, находит и возвращает индекс первого совпадения подстроки в строке str.')
    print('Метод str.replace() вернет копию строки, в которой все вхождения подстроки old заменены на подстроку new.')
    print('Метод str.count() возвращает количество вхождений подстроки sub в строку str в диапазоне индексов [start, end], если они переданы в метод')
    print('Тест:')
    test2 = 'Ботать это круто. Очень круто'
    print(test2 + '.find(круто) = ' + str(test2.find('круто')))
    print(test2 + '.replace(круто, к) = ' + test2.replace('круто', 'к'))
    print(test2 + '.count(круто) = ' + str(test2.count('круто')))
    print()
    print('Введите строку: ')
    tx2 = input()
    print('Для выхода выберите 4')
    print('Выберите метод: ')
    ch = int(input())
    if ch == 1:
        w = input('Какое слово вы хотите найти? ')
        pos = tx2.find(w)
        if pos == -1:
            print('Слово не найдено')
        else:
            print(str(pos) + '-' + str(pos + len(w) - 1))
    elif ch == 2:
        z = input('Выберите слово для замены: ')
        x = input('Выберите новое слово: ')
        print(tx2.replace(z, x))
    elif ch == 3:
        k = input('Выберите слово: ')
        print(tx2.count(k))
    elif ch == 4:
        print('Уровень завершен!')
        return 1
    else:
        print('Нет такого метода')
    return 0


def lvl3():
    print('Метод str.split() возвращает список слов (подстрок) в строке, используя sep в качестве разделителя строки str.')
    print('Метод str.join() возвращает строку, которая является конкатенацией (объединением) всех строк-элементов итерируемого объекта iterable.')
    print('Тест:')
    test3 = '1,2,3,4'
    print(test3 + '.split(,) = ' + str(test3.split(',')))
    print(','.join(['1', '2', '3', '4']) + ' = [1, 2, 3, 4].join(,)')
    print(test3 + '.split(,) + join(-) = ' + '-'.join(test3.split(',')))
    print()
    print('Введите строку: ')
    tx3 = input()
    print('1 - split, 2 - join, 3 - split + join')
    print('Для выхода выберите 4')
    print('Выберите метод: ')
    ch = int(input())
    if ch == 1:
        b = input('Введите символ для разделения: ')
        print(tx3.split(b))
    elif ch == 2:
        v = input('Введите что хотите добавить: ')
        w = tx3.split()
        print(v.join(w))
    elif ch == 3:
        b = input('Введите символ для split: ')
        v = input('Введите символ для join: ')
        print(v.join(tx3.split(b)))
    elif ch == 4:
        print('Уровень завершен!')
        return 1
    else:
        print('Нет такого метода')
    return 0


def lvl4():
    print('Метод str.isdigit() возвращает True, если все символы в строке str являются цифрами и есть хотя бы один символ (строка является не пустой и не состоит из пробелов), в противном случае False.')
    print('Метод строки str.isalpha() возвращает True, если все символы в строке str являются буквенными и есть хотя бы один символ (строка не пустая и не состоит из одного пробела), в противном случае False.')
    print('Метод str.strip() вернет копию строки str с удаленными начальными и конечными символами chars. Другими словами, обрежет строку str с обоих концов. Аргумент chars - это строка, указывающая набор удаляемых символов. Если аргумент chars не задан или None, то по умолчанию удалит пробелы с обоих концов строки.')
    print('Тест:')
    test4 = '12345'
    print(test4 + '.isdigit() = ' + str(test4.isdigit()))
    test4b = 'abc'
    print(test4b + '.isalpha() = ' + str(test4b.isalpha()))
    test4c = '  привет  '
    print(test4c + '.strip() = ' + test4c.strip())
    print('Введите строку: ')
    tx4 = input()
    print('Для выхода выберите 4')
    print('Выберите метод: ')
    ch = int(input())
    if ch == 1:
        print(tx4.isdigit())
    elif ch == 2:
        print(tx4.isalpha())
    elif ch == 3:
        print(tx4.strip())
    elif ch == 4:
        print('Уровень завершен!')
        return 1
    else:
        print('Нет такого метода')
    return 0


def lvl5():
    print('Все методы собраны вместе, любая строка станет прекрасной!')
    print('Введите строку: ')
    tx5 = input()
    print('1 - превращает вашу строку в правильный текст')
    print('2 - открыть меню методов')
    print('3 - выход')
    ch = int(input('Выберите: '))
    if ch == 1:
        print('Работает только для букв')
        print('Тест:')
        test5 = '  .....PYthoN;is;AWEsome  '
        print(test5)
        test5 = test5.strip()
        test5 = test5.lower()
        test5 = test5.replace(';', ' ')
        test5 = test5.replace('.', '')
        test5 = test5.capitalize()
        print(test5)
        print()
        tx5 = tx5.strip()
        tx5 = tx5.lower()
        tx5 = tx5.replace(';', ' ')
        tx5 = tx5.replace('.', '')
        tx5 = tx5.capitalize()
        print(tx5)
        return 0
    elif ch == 2:
        g = 0
        while g == 0:
            print('Выберите метод:')
            print('1 - upper, 2 - lower, 3 - capitalize')
            print('4 - find, 5 - replace, 6 - count')
            print('7 - split, 8 - join, 9 - split + join')
            print('10 - isdigit, 11 - isalpha, 12 - strip')
            print('0 - вернуться в меню уровня')
            m = int(input('Ваш выбор: '))
            if m == 1:
                print(tx5.upper())
            elif m == 2:
                print(tx5.lower())
            elif m == 3:
                print(tx5.capitalize())
            elif m == 4:
                w = input('Какое слово вы хотите найти? ')
                pos = tx5.find(w)
                if pos == -1:
                    print('Слово не найдено')
                else:
                    print(str(pos) + '-' + str(pos + len(w) - 1))
            elif m == 5:
                z = input('Выберите слово для замены: ')
                x = input('Выберите новое слово: ')
                tx5 = tx5.replace(z, x)
                print(tx5)
            elif m == 6:
                k = input('Выберите слово: ')
                print(tx5.count(k))
            elif m == 7:
                b = input('Введите символ для разделения: ')
                print(tx5.split(b))
            elif m == 8:
                v = input('Введите что хотите добавить: ')
                w = tx5.split()
                print(v.join(w))
            elif m == 9:
                b = input('Введите символ для split: ')
                v = input('Введите символ для join: ')
                print(v.join(tx5.split(b)))
            elif m == 10:
                print(tx5.isdigit())
            elif m == 11:
                print(tx5.isalpha())
            elif m == 12:
                tx5 = tx5.strip()
                print(tx5)
            elif m == 0:
                print('Возврат в меню уровня')
                g = 1
            else:
                print('Нет такого метода')
        return 0
    elif ch == 3:
            print('Уровень завершен!')
            return 1
    else:
        print('Нет такого пункта')
    return 0


f = 0
while f == 0:
    print('Пожалуйста, выберите уровень: ')
    a = int(input())
    if a == 1:
        f = lvl1()
    elif a == 2:
        f = lvl2()
    elif a == 3:
        f = lvl3()
    elif a == 4:
        f = lvl4()
    elif a == 5:
        f = lvl5()
    else:
        print('Нет такого уровня')