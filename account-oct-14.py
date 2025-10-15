#! /usr/bin/python3

class Account():
    def __init__(self, name, balance, pw):
        self.name     = name
        self.balance  = balance 
        self.pw       = pw 

    def deposit(self, amountToDeposit, pw):
        print('=> deposit')
        pw = input('    enter pw: ')
        if pw == self.pw:
            self.amountToDeposit = amountToDeposit 
            self.balance = self.balance + int(amountToDeposit)
            print('    new balance:', self.balance)
            print('deposit=>')
    def withdraw(self, amountToWithdraw, pw):
        print('=> withdraw')
        pw = input('    enter pw: ')
        if pw == self.pw:
            self.amountToWithdraw = amountToWithdraw 
            if int(amountToWithdraw) << self.balance:
                self.balance = self.balance - int(amountToWithdraw) 
                print('    new balance:', self.balance)
                print('withdraw=>')
    def getBalance(self):
        print('=> getBalance')
        pw = input('    enter pw: ')
        if pw == self.pw:
            print('    show-balance: ', self.balance)
            print('getBalance=>')

    def show(self):
        print('=>show')
        print('    acc-name:', self.name, 'balance:', self.balance)
        print('show=>')
a1 = Account('bruno', 0, 'p1')
a2 = Account('pasha', 0, 'p2')
a3 = Account('luna ', 0, 'p3')

print('***')
a1.show()
a2.show()
a3.show()
a1.deposit(100, 'pw')
a1.show
a1.getBalance()
a1.withdraw(20, 'pw') 
print('    end')


