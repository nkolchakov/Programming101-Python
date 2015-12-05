import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Niki", 1350, "$")
        self.second_account = BankAccount("Vayne", 0, '$')
        self.account_diff_curr = BankAccount('Georgi', 260, 'e')

    def test_b_account_init(self):
        self.assertEqual(self.account.name, "Niki")
        self.assertEqual(self.account._balance, 1350)
        self.assertEqual(self.account.currency, "$")

    def test_b_account_str(self):
        self.assertEqual(str(self.account), 'Bank account for {} with balance of {}{}'.format(
            self.account.name, self.account._balance, self.account.currency))

    def test_b_account_int(self):
        self.assertEqual(int(self.account._balance), 1350)

    def test_b_account_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account._balance, 1350 + 100)

    def test_b_account_balance(self):
        self.assertEqual(self.account._balance, 1350)

    def test_b_account_withdraw(self):
        self.assertTrue(self.account.withdraw(520))
        self.assertEqual(self.account._balance, 1350 - 520)

    def test_b_account_withdraw_with_no_balance(self):
        self.assertFalse(self.second_account.withdraw(300))

    def test_b_account_transfer_to_with_same_currencies(self):
        self.assertTrue(self.account.transfer_to(self.second_account, 400))
        self.assertEqual(self.account._balance, 1350 - 400)
        self.assertEqual(self.second_account._balance, 0 + 400)

    def test_b_account_transfer_to_with_diff_currencies(self):
        self.assertFalse(self.account.transfer_to(self.account_diff_curr, 400))
        self.assertFalse(self.account_diff_curr.transfer_to(self.account, 600))

        self.assertEqual(self.account._balance, 1350)
        self.assertEqual(self.second_account._balance, 0)

    def test_b_account_history(self):
        history_to_compare = ['Account was created']
        self.account.deposit(320)
        history_to_compare.append('Deposited 320{}'.format(
            self.account.currency))

        self.account.balance()
        history_to_compare.append('Balance check -> {}{}'.format(
            self.account._balance, self.account.currency))

        self.account.withdraw(20)
        history_to_compare.append('20{} was withdrawed'.format(
            self.account.currency))

        # check history when withdraw fail
        self.account.withdraw(100000000)
        history_to_compare.append('Withdraw for {}{} failed.'.format(
                100000000, self.account.currency))

        int(self.account)
        history_to_compare.append('__int__ check -> {}{}'.format(
            self.account._balance, self.account.currency))

        self.account.transfer_to(self.second_account, 400)

        # check other acc transfer history
        self.assertEqual('Transfer from {} for {}{}'.format(
            self.account.name, 400, self.account.currency),
            self.second_account.history()[len(self.second_account.history()) - 1])

        history_to_compare.append('Transfer to {} for {}{}'.format(
            self.second_account.name, 400, self.second_account.currency))
        self.assertEqual(self.account.history(), history_to_compare)

if __name__ == '__main__':
    unittest.main()
