# models/purchase.py
class Purchase:
    def __init__(self, product_id, customer_id, quantity):
        self.product_id = product_id
        self.customer_id = customer_id
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Customer ID: {self.customer_id}, Quantity: {self.quantity}"
