class Account:

    def __init__(self, balance):
        self.__balance = balance

    def setBalance(self, value):
        self.__balance = value

    def getBalance(self):
        return "%.2f" % self.__balance

    def deposit(self):
            x = float(input("Enter the amount you would like to deposit: "))
            if x > 0:
                self.__balance += x
            else:
                print("Cannot deposit a negative number!")

    def withdraw(self):
            x = float(input("Enter the amount you would like to withdraw: "))
            if self.__balance >= x:
                self.__balance -= x
            else:
                print("Insufficient balance.")
