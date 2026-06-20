class Account:
    def __init__(self, account_number, holder_name, transactions):
        self.account_number = account_number
        self.holder_name = holder_name
        self.transactions = transactions
    def suspicious_transaction(self):
        for amount in self.transactions:
            if amount > 100000:
                return True
        return False
    def average_transaction(self):
        return sum(self.transactions) / len(self.transactions)
    def negative_balance_risk(self):
        return sum(self.transactions) < 0
    def transaction_volume(self):
        return sum(abs(amount) for amount in self.transactions)
n = int(input())
accounts = []
highest_volume = 0
highest_account = None
risk_count = 0
for _ in range(n):
    account_number = input()
    holder_name = input()
    transactions = list(map(int, input().split()))
    acc = Account(account_number, holder_name, transactions)
    accounts.append(acc)
    if acc.negative_balance_risk():
        risk_count += 1
    volume = acc.transaction_volume()
    if volume > highest_volume:
        highest_volume = volume
        highest_account = acc
print("Fraud Alerts:")
for acc in accounts:
    if acc.suspicious_transaction():
        print(acc.account_number, acc.holder_name)
print("Average Transaction Amount:")
for acc in accounts:
    print(acc.account_number,
          acc.holder_name,
          f"{acc.average_transaction():.2f}")
print("Negative Balance Risk Accounts:", risk_count)
print("Highest Transaction Volume Account:",highest_account.account_number,highest_account.holder_name,highest_volume)