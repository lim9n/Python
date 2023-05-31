def call():
      print("Calling someone ")
      return "Done"

class Phone:
      price=22000
      name="Samsung"
      color="Blue"
      features=['hammer','camera','speaker']


      def call(self):
            print("Call python")
      

      def send_sms(self,phone,sms):
            text=f'seding sms to: {phone} and the message is: {sms}'
            return text


my_phone=Phone()
print(my_phone.features)
my_phone.call()
result=my_phone.send_sms(2000, 'I want py')
print(result)
     