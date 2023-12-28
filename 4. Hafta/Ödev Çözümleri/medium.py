class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Hesabınıza {amount}TL yatırıldı. Yeni Bakiyeniz: {self.balance}TL")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Hesabınızdan {amount}TL çekildi. Yeni Bakiyeniz: {self.balance}TL")
        else:
            print("Yetersiz Bakiye!")

    def display_info(self):
        print(f"Hesap Sahibi: {self.account_holder}")
        print(f"Bakiye: {self.balance}TL")


class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0, interest_rate = 0.2):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Faiz Eklendi. Yeni Bakiye: ${self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Hesabınızdan {amount}TL çekildi. Yeni Bakiyeniz: {self.balance}TL")
        else:
            print("Para çekme işlemi başarısız, limit aşıldı!")

savings_account = SavingsAccount("Ali", balance=1000)
checking_account = CheckingAccount("Esra", balance=500, overdraft_limit=200)

savings_account.deposit(500)
savings_account.add_interest()
savings_account.display_info()
print("\n")

checking_account.withdraw(300)
checking_account.display_info()
print("\n")

checking_account.withdraw(800)  