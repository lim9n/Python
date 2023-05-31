class Bank:
      def __init__(self,previous_balance):
            self.previous_balance=previous_balance


      def __repr__(self):

            return f'My company name is LIMON _BANK and the balance is {self.previous_balance}'


      # def get_balance(self):
      #       return self.previous_balance
      


      def Deposite(self,amount):
            if amount>0:
                  self.previous_balance+=amount

            return self.previous_balance



dbbl = Bank(5000)
print(dbbl)
dbbl.Deposite(2000)
print(dbbl.Deposite(2000))




