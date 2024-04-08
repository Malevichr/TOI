import random


class Lab8:
    def __init__(self, task: int):
        self.__taskNumber = task

    def start(self):
        match self.__taskNumber:
            case 0:
                self.__task0()
            case 1:
                self.__task1()
            case 2:
                self.__task2()
            case 3:
                self.__task3()
    def __task0(self):
        matrix = [[random.randint(0, 35) for i in range(5)] for i in range(5)]
        a = []
        for i in matrix:
            print(i)
        print(matrix[1][3], matrix[2][0])
        print([matrix[i][1]for i in range(3)])
        print(sum(matrix[2])/3)
        print([(j for j in i if (24 <= j <= 26)) for i in matrix])

    def __task1(self):
        matrix = [[random.randint(0, 10) for i in range(5)] for i in range(5)]
        a = []
        for i in matrix:
            print(i)
            a.append(min(i))
            a.append(max(i))
        print(min(a), max(a))

    def __task2(self):
        matrix = [[random.randint(0, 10) for i in range(5)] for i in range(5)]
        a = []
        maxId = 0
        maxim = 0
        for i in range(5):
            print(matrix[i])
            if (maxim < sum(matrix[i])):
                maxId = i
                maxim = sum(matrix[i])
        print(matrix[maxId])

    def __task3(self):
        matrix = [[random.randint(0, 10) for i in range(5)] for i in range(5)]
        mins = []
        for i in range(5):
            print(matrix[i])
            for j in range(5):
                if (j + i) > 4:
                    mins.append(matrix[i][j])
        print(min(mins))

        times = 1
        for i in [i for i in matrix[-1] if (i != 0)]:
            times *= i
        print(times)
