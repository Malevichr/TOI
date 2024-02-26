from random import randint


class Lab4:
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

    '''Создайте список целых чисел от -20 до 30 (генерация).'''
    def __task1(self):
        print([i for i in range(-20, 30+1)])

    '''Создайте список целых чисел от -10 до 10 с шагом 2 (генерация list).'''
    def __task2(self):
        print(list(i for i in range(-10, 10+1, 2)))

    '''Создайте список из 20 пятерок (генерация).'''
    def __task3(self):
        print([5]*20)

    '''Создайте список из сумм троек чисел от 0 до 10, используя генератор списка (0 + 1 + 2, 1 + 2 + 3, …).'''
    def __task4(self):
        print([str(i) + " + " + str(i+1) + " + " + str(i+2) for i in range(11)])

    '''Заполните массив элементами арифметической прогрессии. 
    Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.'''
    def __task5(self):
        a, b, c = int(input()), int(input()), int(input())
        print([i for i in range(a, a + b*c, c)])

    '''Заполните массив случайными числами в диапазоне 20..100 и подсчитайте отдельно число чётных и нечётных элементов.'''
    def __task6(self):
        a = [randint(20, 100) for i in range(10)]
        c, b = [], []
        for i in a:
            if i % 2 == 0:
                c.append(i)
            else:
                b.append(i)
        print(sum(c))
        print(sum(b))