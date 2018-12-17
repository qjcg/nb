#!/usr/bin/env python3
"""The account module contains classes describing Transactions and Accounts.

This module might be used as follows:

>>> t1 = Transaction(50, '2014-03-02')
>>> t2 = Transaction(70, '2013-03-09')
>>> t3 = Transaction(80, '2015-08-19', 'BTC')
>>> a = Account(90210, "Beverly Hills Bank Account", [t1,t2,t3])
>>> a.balance
200
>>> a.all_usd
False

"""
import pickle

class Transaction:
    """Transaction represents a single financial transaction."""
    def __init__(self, amount, date, currency="USD", conversion_rate=1,
                 description=None):
        self.__amount = amount
        self.__date = date
        self.__currency = currency
        self.__conversion_rate = conversion_rate
        self.__description = description

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__conversion_rate

    @property
    def description(self):
        return self.__description

    @property
    def usd(self):
        return self.__amount * self.__conversion_rate

class Account:
    """Account represents a Canadian bank account."""
    def __init__(self, account_num, account_name, transactions):
        self.__account_num = account_num
        assert len(account_name) >= 4
        self.__account_name = account_name
        self.transactions = transactions

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, new_name):
        assert len(new_name) >= 4
        self.__account_name = new_name

    def __len__(self):
        return len(self.transactions)

    @property
    def balance(self):
        """Get the balance of all transactions in your Account."""
        return sum([t.usd for t in self.transactions])

    @property
    def all_usd(self):
        """Return True if all transactions are in USD, otherwise False."""
        all_t = {t.currency for t in self.transactions}
        #return "USD" in all_t and len(all_t) == 1
        return not all_t - {"USD"}

    def apply(self, t):
        assert isinstance(t, Transaction), "argument must be a Transaction"
        self.transactions.append(t)

    def save(self):
        with open(str(self.__account_num) + '.acc', 'wb') as f:
            data = {'num': self.__account_num,
                    'name':self.account_name,
                    'transactions': self.transactions}
            pickle.dump(data, f)

    def load(self):
        with open(str(self.__account_num) + '.acc', 'rb') as f:
            data = pickle.load(f)
            self.__account_name = data['name']
            self.transactions = data['transactions']

if __name__ == '__main__':
    import doctest
    doctest.testmod()
