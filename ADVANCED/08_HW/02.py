from abc import ABC, abstractmethod

# ================================

class Zombie(ABC):
    def __init__(self):
        self.health = 100
        super().__init__()
    
    @abstractmethod
    def calculate_health(self, second):
        pass

# ================================

class FastZombie(Zombie):
    def __init__(self):
        self.speed = 5
        super().__init__()

    def calculate_health(self, second):
        self.health -= ((second * self.speed) // 10) * 5
        if self.health <= 0:
            return f"the zombie has died"
        return f"remaining health: {self.health}"

# ================================

class SlowZombie(Zombie):
    def __init__(self):
        self.speed = 2
        super().__init__()

    def calculate_health(self, second):
        self.health -= ((second * self.speed) // 10) * 5
        if self.health <= 0:
            return "the zombie has died"
        return f"remaining health: {self.health}"

# ================================

fast = FastZombie()
slow = SlowZombie()
print(fast.calculate_health(40))  # dead
print(slow.calculate_health(10))