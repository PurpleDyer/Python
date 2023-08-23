class Student:
    def __init__(self, name: str, math: int, science: int, art: int, pe: int):
        self.name = name
        self.math = math
        self.science = science
        self.art = art
        self.pe = pe

    def todict(self) -> dict:
        return {
            'math': self.math,
            'science': self.science,
            'art': self.art,
            'pe': self.pe
            }

    def toscore(self, key: str) -> int:
        return self.todict().get(key)

    def average(self) -> int:
        return (self.math + self.science + self.art + self.pe) / 4

student1 = Student("Asghar", 14, 15, 20, 20)

print(student1.toscore("math")) # 14
print(student1.toscore("science")) # 15
print(student1.toscore("art")) # 20
print(student1.toscore("pe")) # 20

print(student1.average())