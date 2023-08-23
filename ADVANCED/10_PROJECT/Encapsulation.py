class WithEncapsulationClass:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

my_instance = WithEncapsulationClass("Matin", 16)

print(my_instance.age)  # 16


