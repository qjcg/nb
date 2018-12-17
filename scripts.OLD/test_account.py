#!/usr/bin/env python3
from Account import Transaction, Account

t1 = Transaction(500, '2014-02-22')
t2 = Transaction(-30, '2015-07-12', 'CAD')
t3 = Transaction(70214, '2015-09-12')
t4 = Transaction(333, '2011-09-12')
t5 = Transaction(123123, '2011-09-12', 'BTC')

a = Account(51422, "John's Bank Account", [t1,t2,t3, t4, t5])
print("Balance:", a.balance)
print("All USD?:", a.all_usd)

#a.save()
a.load()
print("Number of transactions:", len(a))
