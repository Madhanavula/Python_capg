# main.py
from mymodule1 import Product
from mymodule1 import Customer
from mymodule1 import Order
from mymodule1 import PaymentGateway

# Create products
product1 = Product(1, "Laptop", 1000)
product2 = Product(2, "Phone", 500)
product3 = Product(3, "Tablet", 300)

# Create a customer
customer = Customer(1, "John Doe", "john@example.com")

# Create an order
order = Order(101, customer, [product1, product2, product3])

# Create a payment gateway
payment_gateway = PaymentGateway()

# Process payment
payment_result = payment_gateway.process_payment(order, "Credit Card", order.calculate_total())

# Display order summary and payment result
print(order.create_order_summary())
print(payment_result)