class Bank_Account:
    def __init__(self,name):
        self.balance = 0
        self.name = name
        print(self.name," your balance is 0")

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n ",self.name,"Amount deposited: ",amount)


    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn:"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n ",self.name," You withdrew: ",amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=",self.balance)

aris = Bank_Account("aris")
aris.deposit()
aris.withdraw()
aris.display()

baba = Bank_Account("baba")
baba.deposit()
baba.withdraw()
baba.display()
