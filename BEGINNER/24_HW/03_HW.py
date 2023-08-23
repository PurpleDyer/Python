class Car:
    def __init__(self, speed: int):
        self.speed = speed
    
    def __int__(self):
        return self.speed

class Camera:
    def calc(self, car: object):
        if int(car) <= 75:
            return "OK"

        elif int(car) > 75:

            if (int(car)-75)//10 >= 10:
                return("Lisence Suspended") 
            else:
                return (int(car)-75)//10

car1 = Car(50)
car2 = Car(75)
car3 = Car(90)
car4 = Car(125)
car5 = Car(160)
car6 = Car(175)
car7 = Car(300)
camera = Camera()

print(camera.calc(car1))
print(camera.calc(car2))
print(camera.calc(car3))
print(camera.calc(car4))
print(camera.calc(car5))
print(camera.calc(car6))
print(camera.calc(car7))