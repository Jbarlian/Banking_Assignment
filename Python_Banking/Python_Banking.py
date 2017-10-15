from Account import Account
from Customer import Customer
from Bank import Bank


def main():

    bank = Bank("Bank of America")

    while True:
        x = input("[1] Add Customer(s)\n"
                  "[2] Count Customer(s\n"
                  "[3] Print Customer(s)\n"
                  "[4] Set Account\n"
                  "[5] Get Balance\n"
                  "[6] Deposit Money\n"
                  "[7] Withdraw Money\n"
                  "[8] Exit\n")
        if x == "1":
            first = input("Input first name: ")
            last = input("Input last name: ")
            bank.addCustomer(first, last)
        elif x == "2":
            print(bank.getNumOfCustomers(), "Customer(s).")
        elif x == "3":
             y = int(input("Choose which customer to print: "))
             print(bank.getCustomer(y-1).getFirst() + " " + bank.getCustomer(y-1).getLast())
        elif x == "4":
             y = int(input("Choose which customer to set account for: "))
             bal = float(input('Input Balance: '))
             act = Account(bal)
             bank.getCustomer(y-1).setAccount(act)
        elif x == "5":
             y = int(input("Choose which customer to check account for: "))
             print(bank.getCustomer(y-1).getAccount().getBalance())
        elif x == "6":
            y = int(input("Choose which account to deposit: "))
            bank.getCustomer(y-1).getAccount().deposit()
        elif x == "7":
            y = int(input("Choose which account to withdraw: "))
            bank.getCustomer(y-1).getAccount().withdraw()
        elif x == "8":
            break


main()