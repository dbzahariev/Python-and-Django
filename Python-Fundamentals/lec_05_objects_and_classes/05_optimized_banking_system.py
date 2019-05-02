class BankAccount:
    def __init__(self, accountName, Bank, accountBalance):
        self.Name = accountName
        self.Bank = Bank
        self.Balance = float(accountBalance)


data = input()
bank_accounts = []
while not data == 'end':
    data = data.split(' | ')
    bank_accounts.append(BankAccount(Bank=data[0], accountName=data[1], accountBalance=data[2]))
    data = input()

bank_accounts.sort(key=lambda x: (x.Balance, -len(x.Bank)), reverse=True)
for bank_account in bank_accounts:
    print(f'{bank_account.Name} -> {bank_account.Balance:.2f} ({bank_account.Bank})')
