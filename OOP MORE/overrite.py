class Person:
      def __init__(self,name,age,height,weight):
            self.name=name
            self.age=age
            self.height=height
            self.weight=weight
#overwrite 
      def eat(self):
            return ("eat more and more")

      def exercise(self):
            return("Exercise Dorkar nai")

class Cricketer(Person):
      def __init__(self, name,age, height, weight,team):
            self.team=team
            super().__init__(name, age, height, weight)


      def eat(self):
            return ("Eat healthy")
      def exercise(self):
            return ("Everyday")

#     + sign overload

      def __add__(self, other):
            return self.age+other.age   # magic method  __add__ , __mult__ ,  (dunder methods)


Player1=Cricketer("Shakib", 22, 22, 22, "ha")
Player2=Cricketer("abc", 22, 44, 22, "bd")
# print(Player1.eat())
# print(Player1.exercise())

print(Player1+Player2)