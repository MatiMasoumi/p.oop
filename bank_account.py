class BankAccount:
    def __init__(self,accountNumber,balance,password):
        self.accountNumber=accountNumber
        self._balance=balance
        self.__password=password
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,balance):
        if balance>=0:
            self._balance=balance
        else:
            print('Invalid balance')
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        if len(password) >= 8:
            self.__password=password
        else:
            print('password must more than 8')
            