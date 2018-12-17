from Account import Account

a = Account('JGaccount', 444)
a.load()
print(a.__dict__)
print(a._transaction_list[0].amount)
print(a._transaction_list[1].amount)
