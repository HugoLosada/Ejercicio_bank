class bankaccount:
    def __init__(self,account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number
    
    def add_funds(self,funds):
        self.balance = self.balance + funds

    def get_balance(self):
            return self.balance

    

bank_account = bankaccount("ES9483916438918389816483196481619")

bank_account.add_funds(-100)
bank_account.add_funds(1000)


print(f"La cuenta con el número: {bank_account.get_account_number()} tiene {bank_account.get_balance()}€ en su balance")
