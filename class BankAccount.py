class Person:

    def __str__(self):
        return f'{self.name} {self.age}'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello {self.name}!')


class BankAccount:

    def __init__(self, balance, owner):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


owner = Person('Max', 23)
account = BankAccount(1000, owner)
print(account.deposit(500))
print(account.balance)
print(account.withdraw(1000))
print(account.balance)
print(account.owner)