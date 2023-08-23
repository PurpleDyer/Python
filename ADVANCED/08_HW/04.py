class BankAccount:
    def __init__(self, money_amount):
        self.money_amount = money_amount

    def get_money(self, wanted_money):
        if wanted_money > self.money_amount:
            return "not enough money"
        
        self.money_amount -= wanted_money
        fifty = 0
        ten = 0
        five = 0
        total = 0
        while wanted_money != 0:
            if wanted_money >= 50:
                fifty += 1
                wanted_money -= 50
            elif wanted_money >= 10:
                ten += 1
                wanted_money -= 10
            elif wanted_money >= 5:
                five += 1
                wanted_money -= 5
        return f"50toman: {fifty}\n10toman: {ten}\n5toman: {five}"

    def remaining_money(self):
        return f"you have a total of {self.money_amount}toman in your bank account"

# ======================================

bankaccount = BankAccount(200000)
print(bankaccount.get_money(15285))
print(bankaccount.get_money(200000))
print(bankaccount.remaining_money())