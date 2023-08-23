class Cell:
    def __init__(self):
        self.contents = []

    def add_content(self, element):
        self.contents.append(element)

    def remove_content(self, element):
        self.contents.remove(element)

    def __str__(self):
        return "-".join([str(content) for i in self.contents])

class Character:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.char = '0'

class Map:
    def __init__(self):
        self.length = 10
        self.width = 10

    def __str__(self):
        last_string = ""
        for i in range(self.width):
            last_string += "|" + "|".join([str(Cell()).center(4)]*self.length)+"\n"
        return last_string

map1 = Map()
print(map1)