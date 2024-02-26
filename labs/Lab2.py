
class Lab2():
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
            case 6:
                self.__task6()
            case 7:
                self.__task7()
            case 8:
                self.__task8()

    '''Последовательно вводятся ненулевые числа. 
    Определить сумму положительных и сумму отрицательных чисел. 
    Закончить ввод чисел при вводе 0. Для перевода из строки в целое число, 
    использовать функцию int().'''
    def __task1(self):
        a = []
        b, c = [], []
        a.append(int(input()))
        while(a[-1] != 0):
            if (a[-1] > 0 ):
                b.append(a[-1])
            elif (a[-1] < 0):
                c.append(a[-1])
            a.append(int(input()))

        print(sum(b))
        print(sum(c))

    '''При помощи цикла распечатать ряд Фибоначчи:  1 1 2 3 5 8 13 21'''
    def __task2(self):
        a = int(input())
        for i in range(1, a + 1):
            print(self.__fib(i), end= " ")
    def __fib(self, a):
        if (a == 1 or a == 2):
            return 1
        return self.__fib(a - 1) + self.__fib(a - 2)

    '''Запрашиваются 10 чисел (целые значения от 0 до 1000). 
    Опишите алгоритм, позволяющий найти и вывести минимальное 
    значение среди введенных чисел, которые имеют чётное значение и не делятся на три.'''
    def __task3(self):
        a = []
        for i in range(0, 10):
            c = int(input())
            if (c % 2 == 0 and c % 3 != 0):
                a.append(c)
        print(min(a))

    '''Составить программу для вычисления среднеарифметического N произвольных вводимых чисел.'''
    def __task4(self):
        x = int(input())
        a = []
        for i in range(0, x):
            a.append(int(input()))
        print(sum(a)/len(a))
    '''Исправить предыдущее задание (2_3) для работы со случайными числами.'''
    def __task5(self):
        a = []
        for i in range(0, 10):
            c = random.randint(0, 1000)
            if (c % 2 == 0 and c % 3 != 0):
                a.append(c)
        print(min(a))

    '''Найдите все трёхзначные и четырёхзначные числа Армстронга.'''
    def __task6(self):
        a = range(100, 999)
        b = range(1000, 9999)
        tri = []
        chet = []
        for i in a:
            c = str(i)
            x = [int(c[0]), int(c[1]), int(c[2]) ]
            if (x[0]**3 +x[1]**3 + x[2]**3 == i):
                tri.append(i)
        print(tri)
        for i in b:
            c = str(i)
            x = [int(c[0]), int(c[1]), int(c[2]), int(c[3])]
            if (x[0]**4 +x[1]**4 + x[2]**4 + x[3]**4 == i):
                chet.append(i)
        print(chet)
    '''Напишите программу, которая запрашивает натуральное число N и 
    выводит на экран все автоморфные числа, не превосходящие N.'''
    def __task7(self):
        n = int(input())
        a = []
        for i in range(1, n+1):
            if (str(i**2).endswith(str(i))):
                a.append(i)
        print(a)

    '''Распечатывать дни недели с их порядковыми номерами. 
    Кроме того, рядом выводить выходной ли это день или рабочий.'''
    def __task8(self):
        z = 1
        for dni in 'понедельник,', 'вторник,', 'среда,', 'четверг,', 'пятница,', 'суббота,', 'воскресенье,':
            z = str(z)
            if dni in ['суббота,', 'воскресенье,']:
                print(z + '-й', 'день недели -', dni, 'выходной')
            else:
                print(z + '-й', 'день недели -', dni, 'рабочий день')
            z = int(z)
            z += 1