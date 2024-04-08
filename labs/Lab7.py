import random


class Lab7:
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
            case 9:
                self.__task9()
            case 10:
                self.__task10()
    '''Дан массив. Необходимо подтвердить, что в массиве есть числа, кратные трем.'''
    def __task1(self):
        array = [random.randint(0,10) for i in range(5)]
        newArray = [i for i in array if (i % 3 == 0)]
        print(array)
        print(len(newArray) > 0)
    '''Заполните массив случайными числами в диапазоне 0..4 и 
    выведите на экран номера всех элементов, равных значению X (оно вводится с клавиатуры).'''
    def __task2(self):
        array = [random.randint(0, 4) for i in range(5)]
        x = int(input())
        newArray = [i for i in range(len(array)) if (array[i] == x)]
        print(array)
        print(newArray)
    '''Заполните массив случайными числами. Найдите номера первого минимального и последнего максимального элемента массива.'''
    def __task3(self):
        array = [random.randint(0, 4) for i in range(5)]
        maxArray = [i for i in range(len(array)) if (array[i] == max(array))]
        minArray = [i for i in range(len(array)) if (array[i] == min(array))]
        print(array)
        print(maxArray[-1])
        print(minArray[0])

    '''Необходимо написать программу, в которой сортировка выполняется «методом камня» –
     самый «тяжёлый» элемент опускается в конец массива.'''
<<<<<<< HEAD


    def __task4(self):
        array = [random.randint(0, 4) for i in range(5)]
        print(array)
        for i in range(len(array)):
            for j in range(len(array)):
                if (array[i] > array[j]):
                    array[i], array[j] = array[j], array[i]
        print(array)
    '''Необходимо написать программу, которая сортирует массив (быстрой сортировкой) по возрастанию первой цифры числа.'''
=======
>>>>>>> origin/master
    def __qSort(self, A, nStart, nEnd):
        if nStart >= nEnd: return
        L = nStart
        R = nEnd
        X = A[(L + R) // 2]
        while L <= R:
            while A[L] < X: L += 1  # разделение
            while A[R] > X: R -= 1
            if L <= R:
                A[L], A[R] = A[R], A[L]
                L += 1
                R -= 1
        self.__qSort(A, nStart, R)  # рекурсивные вызовы
        self.__qSort(A, L, nEnd)
<<<<<<< HEAD
=======

    def __task4(self):
        array = [random.randint(0, 4) for i in range(5)]
        print(array)
        for i in range(len(array)):
            for j in range(len(array)):
                if (array[i] > array[j]):
                    array[i], array[j] = array[j], array[i]
        print(array)
    '''Необходимо написать программу, которая сортирует массив (быстрой сортировкой) по возрастанию первой цифры числа.'''
>>>>>>> origin/master
    def __task5(self):
        array = [random.randint(0, 4) for i in range(5)]
        print(array)
        self.__qSort(array, 0, len(array) - 1)
        print(array)
    '''Напишите программу, которая, не изменяя заданный массив, 
    выводит номера его элементов в возрастающем порядке. Использовать вспомогательный массив номеров.'''
    def __task6(self):
        array = [random.randint(0, 4) for i in range(5)]
        print(array)
        list = dict((k, array[k]) for k in range(len(array)))
        newDict = {k: v for k, v in sorted(list.items(), key=lambda item: item[1])}
        for i in newDict:
            print(i, newDict[i], sep=", ")
    '''Напишите программу, которая сортирует массив и находит количество различных чисел в нём. Не использовать встроенные функции.'''
    def __task7(self):
        array = [random.randint(0, 4) for i in range(5)]
        newArray = []
        for i in array:
            if not (i in newArray):
                newArray.append(i)
        print(array)
        print(newArray)
    '''Дан массив. Назовем серией группу подряд идущих одинаковых элементов, а длиной серии — количество этих элементов. 
    Сформировать два новых массива, в один из них записывать длины всех серий, а во второй — значения элементов, образующих эти серии.'''
    def __task8(self):
        array = [random.randint(0, 4) for i in range(5)]
        d = dict()
        for e in array:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        print(array)
        for e in d:
            print(e, d[e])
    '''Напишите вариант метода пузырька, который заканчивает работу, 
    если на очередном шаге внешнего цикла не было перестановок. Не использовать встроенные функции.'''
    def __task9(self):
        array = [random.randint(0, 4) for i in range(5)]
        print(array)
        for i in range(len(array) - 1):
            f = True
            for j in range(len(array) - 1 - i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    f = False
            if (not f):
                break
        print(array)
    '''Напишите программу, которая сортирует массив, 
    а затем находит максимальное из чисел, встречающихся в массиве несколько раз. Не использовать встроенные функции.'''
    def __task10(self):
        array = [random.randint(0, 4) for i in range(5)]
        print(array)
        array.sort()
        d = dict()
        for e in array:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        print(array)
        for e in d:
            if (d[e] > 1):
                print(e, d[e])