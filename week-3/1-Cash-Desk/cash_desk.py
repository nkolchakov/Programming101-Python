class Bill:

    def __init__(self, amount):
        self._amount = amount

    def __int__(self):
        return self._amount

    # for dict
    def __repr__(self):
        return str(self)

    def __str__(self):
        return '{}'.format(int(self))

    def __eq__(self, other):
        return self._amount == other._amount

    def __hash__(self):
        return hash(str(self._amount))

    def total(self):
        return int(self._amount)

    def __getitem__(self, index):
        return self._amount

    def papers(self):
        return self

    def __lt__(self, other):
        return self._amount < other._amount


class BatchBill:

    def __init__(self, bills):
        self._bills = bills

    def __len__(self):
        return len(self._bills)

    def total(self):
        print (self._bills)
        return sum(x.total() for x in self._bills)

    def __getitem__(self, index):
        return self._bills[index]

    def __str__(self):
        return '{}'.format(self._amount)

    def __repr__(self):
        return str(self._bills)

    def papers(self):
        return self._bills



class CashDesk:

    def __init__(self):
        self._money = []

    def take_money(self, money):
        if isinstance(money, Bill):
            self._money.append(money)
        else:
            for value in money.papers():
                print (value)
                self._money.append(value)

    def total(self):
        return sum((x.total() for x in self._money))

    def inspect(self):
        values = {}
        for el in self._money:
            if el not in values:
                values[el] = 1
            else:
                values[el] += 1

        return values

def main():

    a = Bill(5)
    b = Bill(7)
    c = Bill(10)

    print (int(a))
    print (str(a))

    print (a == b)

    money_holder = {}
    money_holder[a] = 1
    money_holder[c] = 2

    bills = [a, b, c]

    batch = BatchBill(bills)

    print ('len ' + str((len(batch))))
    print ('total  ' + str(batch.total()))

    if c in money_holder:
        money_holder[c] += 1

    print (money_holder)

    for bill in batch:
        print(bill)

    # values = [10, 20, 50, 100, 100, 100]
    # bills = [Bill(value) for value in values]
    # batch = BatchBill(bills)

    # desk = CashDesk()
    # desk.take_money(a)
    # desk.take_money(batch)
    # desk.take_money(a)
    # print desk.total()
    # print desk.inspect()

    values = [10, 20, 50, 100, 100, 100, 13]
    bills = [Bill(value) for value in values]

    batch = BatchBill(bills)

    dsk = CashDesk()

    dsk.take_money(Bill(10))
    dsk.take_money(batch)
    dsk.take_money(BatchBill([Bill(12), Bill(13)]))

    print(dsk.total())  # 390
    print (dsk.inspect())

if __name__ == '__main__':
    main()
