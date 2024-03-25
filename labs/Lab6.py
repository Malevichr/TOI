import random


class Lab6:
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
    def __task1(self):
        str = "1+25+3"
        summands = map(int, str.split("+"))
        print(sum(summands))
    def __task2(self):
        myList = [random.randint(0, 10) for i in range(5)]
        myList.sort()
        print(myList)
        print(min(myList), max(myList))
        print(sum(myList), sum(myList) / len(myList))

        print(myList[1])
    def __task3(self):
        str = input()
        print(str[::-1] == str)
    def __simpleInt(self, a):
        k = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                k = k + 1
        if (k <= 0):
            return True
        else:
            return False
    def __task4(self):
        myList = [random.randint(0, 10) for i in range(5)]
        newList = [i for i in myList if (self.__simpleInt(i))]
        print(myList, newList, sep="\n")
    def __task5(self):
        try:
            N = int(input("Введите N: "))
        except Exception as e:
            print(e)
        a = []
        i = 0
        print("Введите числа")

        while (i < N):
            try:
                a.append(int(input()))
                i += 1
            except Exception as e:
                print(e)

        print(*a)
        print(f'Sred: {sum(a) / N}')
    def __task6(self):
        a = [random.randint(-20, 20) for i in range(20)]
        print(*a)
        mn = int(input("min = "))
        mx = int(input("max = "))
        indexes = []

        for i in range(len(a)):
            if (mn <= a[i] <= mx):
                indexes.append(i)

        print(f'Length: {len(indexes)}')
        print(f'Indexes: {indexes}')
    def __task7(self):
        a = [random.randint(-20, 20) for i in range(20)]
        print(*a)
        mn = int(input("min = "))
        mx = int(input("max = "))
        indexes = []

        i = 0
        j = 0

        while (i < len(a)):
            if (mn <= a[i] <= mx):
                indexes.append(i + j)
                a.pop(i)
                j += 1
            else:
                i += 1

        print(*a)
        print(f'Length: {len(indexes)}')
        print(f'Indexes: {indexes}')