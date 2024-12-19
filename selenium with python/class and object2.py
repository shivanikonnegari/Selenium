class Product:
    def _init_(self, name,price):
        self.name=name
        self.price=price

class ShoppingCart:
    def _init_(self):
        self.cart=[]

    def add_product(self,product):
        self.cart.append(product)
        print(f"Added {product.name} to the cart.")
    def remove_product(self,product_name):
        for product in self.cart:
            if product.name==product_name:
                self.cart.remove(product)
                print(f"removed {product.name} from the cart")
                return
        print(f"Product {product_name} not found in the cart")
    def calculate_total(self):
        total=sum(product.price for product in self.cart)
        print(f"Total amount:{total:.2f}")
product1=Product(name="laptop",price=1)
product2=Product(name="mouse",price=2)
product3=Product(name="keyboard",price=3)
cart=ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
cart.calculate_total()
cart.remove_product("mouse")
cart.calculate_total()