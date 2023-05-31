class Calculator:
      Brabnd="Casio 99FX"

      def add(self,num1,num2):
            result=f'the result is = {num1+num2}'
            return result
      
      def sub(self,num1,num2):
            result=f'the result is = {num1-num2}'
            return result

      def mal(self,num1,num2):
            result=f'the result is = {num1*num2}'
            return result

      def div(self,num1,num2):
            result=f'the result is = {num1//num2}'
            return result


my_cal=Calculator()

print(my_cal.Brabnd)
 

print(my_cal.add(5, 10))

print(my_cal.div(15, 5))

print(my_cal.mal(5, 5))

print(my_cal.sub(10, 5))