class Person:
      Country="Bangladesh"


      def __init__(self,name,color, height_in_m):
            self.name=name
            self.color=color
            self.height_in_m=height_in_m

      

person1=Person("Limon", "black", 2)
person2=Person("Nishan", "white", 5)



print(person1.color,person1.Country,person1.height_in_m,person1.name)
print(person2.name,person2.Country)