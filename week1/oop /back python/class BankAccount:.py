class BankAccount:
    def __init__(self,holder_name,initial_balance=0):
        self.holder_name=holder_name
        self.initial_balance=initial_balance

    def Deposit_money(self,money):
        self.initial_balance+=money

    def withdraw_money(self,money):
        if(self.initial_balance==0):
            print("you don't have money")
        else:
           self.initial_balance-=money
           
    def check_balance(self):
        print(self.initial_balance)


Account1=BankAccount("Ahmed")

Account1.check_balance()
print("************************")

Account1.withdraw_money(300)
Account1.Deposit_money(200)
Account1.Deposit_money(300)
Account1.check_balance()
Account1.withdraw_money(300)
Account1.check_balance()


    



