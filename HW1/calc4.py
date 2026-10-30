#необычный калькулятор, решающий условную задачу, тут для производства соков
class cl:
#создание базовых ф-ций калькулятораб которые будут использованы в посчетах
    def __init__(self):
        self.res = 0

    def p(self, x, y):
        return x + y

    def m(self, x, y):
        return x - y

    def pr(self, x, y):
        return x * y

    def d(self, x, y):
        return x / y
# calc = cl()
# print(calc.pr(10, 4)) #(тесты)

class ju:
#внос инф-ции про соки
    def __init__(self, n, s, cost, price):
        self.n = n
        self.s = s
        self.cost = cost
        self.price = price

class jucl:
#сам "необычный" калькулятор, рассчитывает прибыль и норму потребелния по колву сахара для условного производителя
    def __init__(self):
        self.calc = cl()
        self.jus = [ju('Яблочный', 12, 40, 90), ju('Апельсиновый', 8, 50, 110), ju('Вишневый', 9, 60, 130)]
        self.sn = 80

    def run(self):
        while True:
            print('1.Прибыль  2.Сахар  3.Выход')
            ch = str(input('Выбор: '))
            if ch == '3':
                print('До свиданья!')
                break
            print('Соки:')
            for i in range(len(self.jus)):
                print(str(i+1) + '. ' + self.jus[i].n)
            ju = self.jus[int(input('Номер: ')) - 1]
            ob = float(input('Объем: '))
            if ch == '1':
                cost1 = self.calc.pr(ju.cost, ob)
                price1 = self.calc.pr(ju.price, ob)
                v = self.calc.m(price1, cost1)
                print('Затраты: ' + str(cost1) + ' руб')
                print('Цена: ' + str(price1) + ' руб')
                print('Выгода: ' + str(v) + ' руб')
            if ch == '2':
                su = self.calc.pr(self.calc.d(ju.s, 100), ob)
                sugr = self.calc.pr(su, 1000)
                ost = self.calc.m(self.sn, sugr)
                print('Сахар: ' + str(sugr) + ' г')
                print('Норма: ' + str(self.sn) + ' г')
                if ost < 0:
                    print('Норма превышена!')
                elif ost == 0:
                    print('Идеально, остановитесь сейчас!')
                else:
                    print('Осталось: ' + str(ost) + ' г')

calc = jucl()
calc.run()
