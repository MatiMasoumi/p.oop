from bank_account import BankAccount
#from saving_account import SavingAccount

account=BankAccount(12345,1000,'mypass')
print('Account Number:', account.accountNumber)

print('Balance:', account.balance)
account.balance=2000
print('update Balance:', account.balance)

account.password='12345'
print('Password:', account.password)
account.password='newpassword123'
print('update Password:', account.password)
#saving_account=SavingAccount(6532145,5000,'sequenceword',0.05)
#saving_account.access_balance_password()