from Customer import Customer

class Bank:

    def __init__(self, bankname):
        self.__bankname = bankname
        self.__customer = []

    def addCustomer(self, first, last):
        self.__customer.append(Customer(first, last))

    def getNumOfCustomers(self):
        return len(self.__customer)

    def getCustomer(self, index):

        for i in range(len(self.__customer)):
            if i == index:
                return self.__customer[i]



