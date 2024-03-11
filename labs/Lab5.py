from datetime import date


class Lab5:
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

    def __task1(self):
        str = input()
        print(str[:8], str[len(str) // 2 - 2: len(str) // 2 + 2], str[-5:], sep="\n")

    def __task2(self):
        str = input()
        print(str[::-1])

    def __task3(self):
        str = input()
        print(str[::2])

    def __task4(self):
        str = input()
        print(str[::2], str[1::2], sep="")

    def __task5(self):
        nowDate = date.today()
        dateStr = map(str, [nowDate.day, nowDate.month, nowDate.year])
        print("/".join(dateStr))

    def __task6(self):
        str = "c:/изображения/2018/1.jpg"
        str = str.replace("/", "\n")
        print(str)

    def __task7(self):
        str = "1+25+3"
        summands = map(int, str.split("+"))
        print(sum(summands))
    def __task8(self):
        str = input()
        print(str[::-1] == str)
