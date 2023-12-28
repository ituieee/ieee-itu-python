class Product:
    total_products = 0

    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        Product.total_products += 1

    def apply_discount(self, discount_percentage):
        discounted_price = self.price * (1 - discount_percentage / 100)
        return discounted_price

    @classmethod
    def special_deals(cls, discount_threshold):
        special_deals = [product for product in cls.products if product.apply_discount(0) > discount_threshold]
        return special_deals

    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock Quantity: {self.stock_quantity}\n")


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def view_products(self, products):
        for product in products:
            product.display_info()

    def add_to_cart(self, product, quantity=1):
        self.shopping_cart.add_item(product, quantity)

    def place_order(self):
        self.shopping_cart.display_cart()
        print(f"Total Price: ${self.shopping_cart.calculate_total():.2f}")
        print("Order placed successfully!\n")


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.stock_quantity >= quantity:
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
            product.stock_quantity -= quantity
            print(f"{quantity} {product.name}(s) added to the cart.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def display_cart(self):
        print("Shopping Cart:")
        for item_name, item_data in self.items.items():
            print(f"{item_data['quantity']} {item_name}(s) - ${item_data['product'].price:.2f} each")

    def calculate_total(self):
        total_price = sum(item_data['quantity'] * item_data['product'].price for item_data in self.items.values())
        return total_price



product1 = Product("Laptop", 1200, 10)
product2 = Product("Smartphone", 800, 15)
product3 = Product("Headphones", 100, 20)

customer = Customer("Umur Ata", "umur_ata@gmail.com")

customer.view_products([product1, product2, product3])

customer.add_to_cart(product1, 2)
customer.add_to_cart(product2, 1)


customer.place_order()


Product.products = [product1, product2, product3]  
special_deals = Product.special_deals(discount_threshold=10)

print("\nSpecial Deals:")
for deal in special_deals:
    deal.display_info()