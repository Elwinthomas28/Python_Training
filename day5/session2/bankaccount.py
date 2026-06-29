class bankaccount:
    def __init__(self,balance,name):
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("invalid bank account")
account=bankaccount(500,"bavith")
print(account.get_balance())
account.set_balance(500)
print("total after adding",account.get_balance())
