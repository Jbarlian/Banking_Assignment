from Account import Account

class Customer:

    def __init__(self, first, last):
        self.__first = first
        self.__last = last
        self.__account = Account(0)

    def getFirst(self):
        return self.__first

    def getLast(self):
        return self.__last

    def getAccount(self):
        return self.__account

    def setAccount(self, account):
        self.__account = account