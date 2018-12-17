from Account import Account, Transaction

a = Account('JGaccount', 123)
t1 = Transaction(52.5, '2014-03-22', 'BTC', 22, 'deposited a bunch of BTC')
t2 = Transaction(-100, '2014-03-27', 'CAD', 0.89, 'withdrew money for beer')

a.apply(t1)
a.apply(t2)
a.save()
