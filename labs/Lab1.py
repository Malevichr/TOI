import calendar


class Lab1:
    def __init__(self, task: int):
        self.__taskNumber = task

    def start(self):
        match self.__taskNumber:
            case 1:
                self.__task1()
            case 2:
                self.__task2()
            case 3:
                self.__task3()
            case 4:
                self.__task4()
            case 5:
                self.__task5()

    def __convert_to(self, num, base, upper=False):
        digits = '0123456789abcdefghijklmnopqrstuvwxyz'
        if base > len(digits): return None
        result = ''
        while num > 0:
            result = digits[num % base] + result
            num //= base
        return result.upper() if upper else result

    ''' Даны две переменные. Запросить их значение. 
    Выполнить основные арифметические действия с переменными,
    целочисленное деление, возведение в квадрат. 
    Осуществить перевод в системы счисления. Вывести результат.'''
    def __task1(self):
        a = int(input())
        b = int(input())
        print(a + b)
        print(a - b)
        print(a * b)
        print(a % b)
        print(a**2)
        print(self.__convert_to(a, b))

    '''Напишите программу, которая определяет, 
    верно ли, что введённое число – трёхзначное. '''
    def __task2(self):
        print(len(str(int(input()))) == 3)

    '''В зависимости от ввода вычислить массу, 
    плотность или объем. Для расчетов использовать формулу m = Vρ '''
    def __task3(self):
        a = {"m", "V", "p"}
        print("Выбирите что вычилсить: ", a)
        match input():
            case "m":
                print("Введите V и p")
                print(int(input())*int(input()))
            case "V":
                print("Введите m и p")
                print(int(input())/int(input()))
            case "p":
                print("Введите m и V")
                print(int(input()) / int(input()))

    '''Вводится год. Определить, является ли он високосным или обычным. 
    Примечание. Високосными являются года, которые делятся на 4, 
    за исключением столетий, которые не делятся на 400.'''
    def __task4(self):
        print(calendar.isleap(int(input())))

    '''Даны катеты прямоугольного треугольника. 
    Найдите площадь, периметр и гипотенузу треугольника.'''
    def __task5(self):
        a, b = map(int, input().split())
        print("S = ", a*b/2)
        print("P = ", a + b + (a ** 2 + b ** 2) ** 0.5)
        print("c = ", (a**2 + b**2)**0.5)