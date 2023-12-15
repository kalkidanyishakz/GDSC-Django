import unittest
from bankAccount import BankAccount

'''
Write unit tests for the "BankAccount" class from Exercise 3.
Test deposit, withdrawal, and balance-related methods to ensure they behave as expected.

holder_name, holder_age,  holder_phone, 
initial_amount, account_number
'''

class TestBankAccount(unittest.TestCase):
    def test_initial_amount(self):
        inital_balance=20
        my_balance=BankAccount('kal', 21, '09092933', inital_balance, 1002484)
        self.assertEqual(my_balance._balance, 20, f'Initial balance should be {inital_balance}')
    
    def test_deposit(self):
        my_balance=BankAccount('kal', 21, '09092933', 0, 1002484)
        my_balance.deposit(200)
        self.assertEqual(my_balance._balance, 200, f'balance should be 200 after deposite')
        self.assertEqual(my_balance._balance, 200, f'balance should be 200 after deposite')
        
    def test_withdraw(self):
        my_balance=BankAccount('kal', 21, '09092933', 300, 1002484)
        my_balance.withdraw(250)
        self.assertEqual(my_balance._balance, 50, f'balance should be 50 after withdrawing 250 from the inital balance of 300 ')
    
    def test_withdraw_more_than_balance(self):
        my_balance=BankAccount('kal', 21, '09092933', 300, 1002484)
        my_balance.withdraw(450)
        self.assertEqual(my_balance._balance, 300, f'account should not withdraw when withdraw amount is greater than the balance')
        
    
if __name__ == '__main__':
    unittest.main()
        