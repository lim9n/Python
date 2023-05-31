class Shop:
      shopping_mall="Basundhara"

      def __init__(self,buyer):
            self.buyer=buyer
            self.cart=[]

      
      def add_to_cart(self,items):
            self.cart.append(items)




Buyer1=Shop("Faiza")


Buyer1.add_to_cart("Bra")
Buyer1.add_to_cart("Penty")

print(Buyer1.cart)


Buyer2=Shop("Orny")

Buyer2.add_to_cart("Dildo")
Buyer2.add_to_cart("Condoms")

print(Buyer2.cart)