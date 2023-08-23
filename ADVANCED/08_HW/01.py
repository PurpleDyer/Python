from abc import ABC, abstractmethod
import math

# ======================================

class Object(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def p(self):
        pass

    @abstractmethod
    def s(self):
        pass

# ======================================

class Circle(Object):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def p(self):
        return (2 * self.radius) * math.pi

    def s(self):
        return (2 ** self.radius) * math.pi

# =====================================

class Rectangle(Object):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def p(self):
        return 2 * (self.width + self.height)

    def s(self):
        return self.width * self.height

# =====================================

# testing...
# Circle
radius = int(input("Please enter radius: "))
circle = Circle(radius=radius)
print(f"circle p: {circle.p()}")
print(f"circle s: {circle.s()}")
print('---------')

# Rectangle
width = int(input("Please enter width: "))
height = int(input("Please enter height: "))
rectangle = Rectangle(width=width, height=height)
print(f"rectangle p: {rectangle.p()}")
print(f"rectangle s: {rectangle.s()}")