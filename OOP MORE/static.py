class Shopping:
      cart=[]
      origin="china" #class attribute / static attribute

      def __init__(self,name,location):
            self.name='Basundhara'  #instance attribute
            self.location="BTC"
      
      def Purchase(self,item,price,amount):
            remaining=amount-price

            if amount>price:
                  return f'buying {item} at a price of {price} and remaining price is  {remaining}'
            else:
                  return f'your account balance is low'
      @staticmethod
      def mul(a,b):
            return a*b
      @classmethod 
      def showing(self,item):
            return("hudai dekhte aschi")
            


mizan=Shopping("basundhara", "BTC")

print(mizan.Purchase("lungi", 400, 100))

print(Shopping.mul(3,4)) 
