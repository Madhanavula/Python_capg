
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_product_info(self):
        return f"Product: {self.name}, Price: ${self.price}"


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def get_customer_info(self):
        return f"Customer: {self.name}, Email: {self.email}"


class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products

    def calculate_total(self):
        total = sum(product.price for product in self.products)
        return total

    def create_order_summary(self):
        product_list = "\n".join([product.name for product in self.products])
        return f"Order ID: {self.order_id}\nCustomer: {self.customer.name}\nProducts:\n{product_list}\nTotal: ${self.calculate_total()}"


class PaymentGateway:
    def process_payment(self, order, payment_method, amount):
        # Simulate payment processing
        return f"Payment processed for Order {order.order_id} using {payment_method} - Amount: ${amount}"





