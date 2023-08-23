class Car:
    def __init__(self, distance, oil):
        self.distance = distance
        self.oil = oil

    def calc(self):
        if self.oil * 10 >= self.distance:
            return True
        else:
            return f"False, oil needed: {self.distance//10 - self.oil}"

car1 = Car(60, 6)
car2 = Car(25, 3)
car3 = Car(90, 6) 
car4 = Car(10, 0.5)

print(car1.calc()) # True
print(car2.calc()) # True
print(car3.calc()) # False, 3
print(car4.calc()) # False, 0.5