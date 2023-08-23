class BankAccount:
    def __init__(self, money: int):
        self.money = money
    
    def get_money(self, money: int):
        if money > self.money:
            return "You dont have enough money to do that"
        else:
            self.money -= money
            fifty = 0
            ten = 0
            five = 0
            one = 0

            while money > 0:
                if not money-50 < 0:
                    money -= 50
                    fifty += 1
                elif not money-10 < 0:
                    money -= 10
                    ten += 1
                elif not money-5 < 0:
                    money -= 5
                    five += 1
                else:
                    break

            return f"50toman: {fifty}\n10toman: {ten}\n5toman: {five}"

    def remaining_money(self):
        return f"Remaining Money: {self.money}"

person1 = BankAccount(200)
person2 = BankAccount(9999)

# print(person1.get_money(300))
print(person2.get_money(2175))
print(person2.get_money(5000))
print(person1.get_money(145))
print(person2.remaining_money())
print(person1.remaining_money())