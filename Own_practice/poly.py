class  Monster:
    def __init__(self, name) -> None:
        self.name = name
    
    def make_sound(self):
        print('Dinosur makes sound')

class Dinosour(Monster):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('Hisshhhhhhh')

class Rinosour(Monster):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('shhiiiiiish')

Monster1=Monster('schooby')
Monster1.make_sound()
Monster2 = Dinosour('Tom')
Monster2.make_sound()

Monster3 = Rinosour('Jerry')
Monster3.make_sound()
