import sys
import unittest
import os

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', 'asdaFGG45g*&')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    @classmethod
    def tearDownClass(cls):
        os.remove("bank.db")

    def test_register(self):
        sql_manager.register('Dinko', 'asdaFGG45g*&')

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', 'asdaFGG45g*&'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', 'asdaFGG45g*&')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_with_username_injection(self):
        logged_user = sql_manager.login('\' OR 1=1 --', '123')
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', 'ggggg32As*&')
        self.assertFalse(logged_user)

    def test_register_with_valid_password(self):
        successfully_reg = sql_manager.register("tester", "asdaFGG45g*&")
        self.assertTrue(successfully_reg)

    def test_register_with_not_long_enough_password(self):
        successfully_reg = sql_manager.register("tester", "sA3%")
        self.assertFalse(successfully_reg)

    def test_register_with_no_capital_letters_password(self):
        successfully_reg = sql_manager.register("tester", "asdfghjk123%")
        self.assertFalse(successfully_reg)

    def test_register_with_no_special_symbols_letters_password(self):
        successfully_reg = sql_manager.register("tester", "asdFGsGH123")
        self.assertFalse(successfully_reg)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', 'asdaFGG45g*&')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', 'asdaFGG45g*&')
        new_password = "mvxza23g5g!~"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

if __name__ == '__main__':
    unittest.main()