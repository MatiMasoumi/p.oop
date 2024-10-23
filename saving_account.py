from bank_account import BankAccount

class SavingAccount(BankAccount):
    def __init__(self, accountNumber, balance, password,interestRate):
        super().__init__(accountNumber, balance, password)
        self.interestRate=interestRate
    def access_balance_password(self):
        print('balance:', self.balance)
        print('password:', self.password)
        