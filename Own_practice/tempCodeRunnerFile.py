class Arthropoda:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is {self.age} years old and he is eating mango.")


class Mammalia(Arthropoda):
    def __init__(self, name, age):
        super().__init__(name, age)

    def drive(self):
        print(f"{self.name} is {self.age} years old and he is driving a car.")


class Man(Mammalia):
    def __init__(self, name, age):
        super().__init__(name, age)

    def talk(self):
        print(f"{self.name} is {self.age} years old and he is talking to his mother.")


man1 = Man("Virat Kohli", 22)
man1.eat()
man1.drive()
man1.talk()
