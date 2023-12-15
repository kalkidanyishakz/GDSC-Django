class BankAccount:
    def __init__(self, holder_name, holder_age,  holder_phone, initial_amount, account_number):
        self.holder_name=holder_name
        self.holder_age=holder_age
        self.holder_phone=holder_phone
        self._balance=initial_amount
        self._account_number=account_number
    
    def display_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance+=amount
        
    def withdraw(self, amount):
        if amount>self._balance:
            print(f'insufficient balance: admasu :) you have only {self._balance} birr')
        else:
            self._balance-=amount
            return amount
    
abebe=BankAccount('abebe teferi', 19, '090972921', 300, 100034954)

abebe.deposit(200)
abebe.withdraw(700)

print(abebe.display_balance())
        

    
#Implement methods for deposit, withdrawal, and displaying the balance. Use encapsulation to protect the balance attribute.
