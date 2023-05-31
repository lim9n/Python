class Product:
    def __init__(self, name):
        self.name = name

class Shop(Product):
    def __init__(self, name):
        self.products = []
        super().__init__(name)

    def add_product(self, product):
        self.products.append(product)

    def buy_product(self, product_name):
        for product in self.products:
            if product == product_name:
                self.products.remove(product)
                return f"Congratulations!"
        return f"Sorry, not available."

shop = Shop("Iphone")

shop.add_product("Iphone")
shop.add_product("Apple")

result = shop.buy_product("Apple")
print(result)

