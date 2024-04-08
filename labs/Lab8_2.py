import random

import numpy


class Lab8_2:
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
            case 11:
                self.__task11()
            case 12:
                self.__task12()

    def __task1(self):
        matrix = [[0 for i in range(4)] for i in range(3)]
        for i in matrix:
            i[0] = 1
            print(i)

    def __task2(self):
        matrix = [[random.randint(0, 9) for i in range(3)] for i in range(2)]
        for i in matrix:
            print(i)

    def __task3(self):
        matrix = [[random.randint(0, 9) for i in range(5)] for i in range(5)]
        print(matrix[0])
        print(matrix[-1])

    def __task4(self):
        matrix = [[random.randint(0, 9) for i in range(5)] for i in range(5)]
        for i in matrix:
            print(i)
        print("")
        for i in range(0, len(matrix), 2):
            print(matrix[i])

    def __task5(self):
        matrix = [[random.randint(0, 9) for i in range(5)] for i in range(5)]
        trans = numpy.transpose(matrix)
        for i in matrix:
            print(i)
        print("")
        for i in range(1, len(matrix), 2):
            if (trans[i][0] > trans[i][-1]):
                print(trans[i])

    def __task6(self):
        matrix = [[random.randint(-10, 10) for i in range(5)] for i in range(5)]
        a = []
        for i in matrix:
            print(i)
            for j in i:
                if (j < 0 and j % 2 == 1):
                    a.append(abs(j))
        print(sum(a))

    def __task7(self):
        matrix = [[random.randint(-10, 10) for i in range(5)] for i in range(5)]
        c = 0
        for i in matrix:
            print(i)
            for j in i:
                if (j == 7):
                    c += 1
        print(c)

    def __task8(self):
        n = 5
        matrix = [[random.randint(-10, 10) for i in range(n)] for i in range(n)]
        a = []
        for i in range(n):
            a.append(matrix[i][i])
        print(a)

    def __task9(self):
        n = 5
        matrix = [[random.randint(-10, 10) for i in range(n)] for i in range(n)]
        trans = numpy.transpose(matrix)
        k = int(input())
        p = int(input())
        print(matrix[k])
        print(trans[p])

    def __task10(self):
        m = 5
        n = 5

        matrix = [[random.randint(-10, 10) for i in range(n)] for i in range(m)]
        for i in matrix:
            print(i)
        print("")
        for i in range(m):

            if(i % 2 == 0):
                print(matrix[i])
            else:
                matrix[i].reverse()
                print(matrix[i])

    def __task11(self):
        m = 5
        n = 5

        matrix = [[0 for i in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if (i % (n-1) == 0) or (j % (n-1) == 0):
                    matrix[i][j] = 1
            print(matrix[i])

    def __task12(self):
        n = 5
        matrix = [[1 for i in range(n)] for i in range(n)]
        for i in range(n):
            matrix[i][i] = 3
            for j in range(i + 1, n):
                matrix[i][j] = 2
        for i in matrix:
            print(i)
    


