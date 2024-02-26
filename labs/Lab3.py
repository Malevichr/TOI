class Lab3:
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

    '''Напишите процедуру, которая выводит на экран в столбик все цифры переданного ей числа, начиная с последней.'''

    def __task1(self):
        self.__task1Procedure(str(int(input())))

    def __task1Procedure(self, number):
        if len(number) > 0:
            print(number[-1])
            self.__task1Procedure(number[0:-1])

    '''Напишите процедуру, которая выводит на экран все делители переданного ей числа (в одну строчку).'''

    def __task2(self):
        self.__task2Procedure(int(input()))

    def __task2Procedure(self, number: int):
        print(1, end=' ')
        for i in range(2, number):
            if (number % i == 0):
                print(i, end=' ')

    '''Составить программу с процедурой для вычисления степени числа (входные параметры: число и степень).'''

    def __task3(self):
        print(self.__task3Procedure(int(input()), int(input())))

    def __task3Procedure(self, number: int, degree: int):
        return number ** degree

    '''Напишите процедуру, которая принимает параметр – натуральное число N – и выводит первые N чисел Фибоначчи.'''

    def __task4(self):
        self.__task4Procedure(int(input()))

    def __task4Procedure(self, number: int):
        a = number
        for i in range(1, a + 1):
            print(self.__fib(i), end=" ")

    def __fib(self, a):
        if a == 1 or a == 2:
            return 1
        return self.__fib(a - 1) + self.__fib(a - 2)
