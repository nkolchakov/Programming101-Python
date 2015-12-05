class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self._balance = balance
        self.currency = currency
        self._history = ['Account was created']

    def deposit(self, amount):
        self._balance += amount
        self._history.append('Deposited {}{}'.format(
            amount, self.currency))

    def balance(self):
        self._history.append('Balance check -> {}{}'.format(
            self._balance, self.currency))
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            self._history.append('Withdraw for {}{} failed.'.format(
                amount, self.currency))
            return False
        else:
            self._balance -= amount
            self._history.append('{}{} was withdrawed'.format(
                amount, self.currency))

            return True

    def __str__(self):
        return 'Bank account for {} with balance of {}{}'.format(
            self.name, self._balance, self.currency)

    def __int__(self):
        self._history.append('__int__ check -> {}{}'.format(
            self._balance, self.currency))

        return self._balance

    def transfer_to(self, account, amount):
        if (self.currency != account.currency):
            return False

        self._balance -= amount
        account._balance += amount

        self._history.append('Transfer to {} for {}{}'.format(
            account.name, amount, self.currency))
        account._history.append('Transfer from {} for {}{}'.format(
            self.name, amount, self.currency))

        return self.currency == account.currency

    def history(self):
        return self._history

# ba = BankAccount('niki', 1000, '$')
# # ba.deposit(100)
# # ba.balance()
# # int(ba)
# ba.withdraw(3000)
# print (ba.history())

# rado = BankAccount("Rado", 1000, "BGN")
# ivo = BankAccount("Ivo", 0, "EUR")
# print (rado.transfer_to(ivo, 500))

# print (rado.balance())
# print (ivo.balance())

# print (rado.history())
# print (ivo.history())
