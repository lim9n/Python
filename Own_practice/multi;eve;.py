class Arthropoda:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is {self.age} years age and he/she is eating mango.")


class Mammalia(Arthropoda):
    def __init__(self, name):
        super().__init__(name,age)

    def drive(self):
        print(f"{self.name} is {self.age} years age and he/she isdriving a car.")


class Man(Mammalia):
    def __init__(self, name,age):
        super().__init__(name,age)

    def talk(self):
        print(f"{self.name} is {self.age} years age and he/she is talking to his/her mother.")

my_dog = Man("Limon",22)
my_dog.eat()
my_dog.drive()
my_dog.talk()
