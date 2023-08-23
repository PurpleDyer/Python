from abc import ABC, abstractmethod

# ===============================

class Heart:
    def __init__(self, litre):
        self.litre = litre

    def calculate(self, minute):
        return self.litre * minute

# ================================

class Person:
    def __init__(self, litre):
        self.litre = litre
        self.heart = Heart(self.litre)

    @abstractmethod
    def calculate_amount(self, minute):
        pass

# ================================

class DiabetesPerson(Person):
    def __init__(self):
        super().__init__(4)

    def calculate_amount(self, minute):
        return self.heart.calculate(minute)

# ================================

class NormalPerson(Person):
    def __init__(self):
        super().__init__(5) 

    def calculate_amount(self, minute):
        return self.heart.calculate(minute)

# =================================

normal = NormalPerson()
diabetes = DiabetesPerson()
print(f"normal person: {normal.calculate_amount(15)}")
print(f"diabetes person: {diabetes.calculate_amount(15)}")