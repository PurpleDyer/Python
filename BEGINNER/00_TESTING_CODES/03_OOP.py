class Car:
    car_type = "speedy"

    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed


    def __str__(self):
        return f"The car is a {self.age} year old {self.name} with around {self.speed}mph speed which is a {self.car_type} car!"


    def speak(self):
        return f"Wassup my nigga"


Bugatti = Car("Bugatti", 9, 300)

print(Bugatti.name)
print(Bugatti.age)
print(Bugatti.speed)
print(Bugatti.car_type)

Bugatti.age = 11
print(Bugatti.age)
Bugatti.car_type = "very speedy"
print(Bugatti.car_type)

# print(Bugatti.info())    not when you have a __str__()

print(Bugatti)

print(Bugatti.speak())