class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Остаток на счете: {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Недостаточно денег на счете")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы сняли {money} рублей. Остаток на счете: {self.balance}")

    def all_balance(self):
        print(f"Остаток на счете: {self.balance}")

man = Account("12345", 600)

man.all_balance()
man.withdraw(450)
man.withdraw(600)
man.all_balance()
man.deposit(10000)
man.all_balance()


