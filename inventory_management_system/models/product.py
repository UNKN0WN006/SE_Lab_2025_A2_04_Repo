class Product:
    def __init__(self, id, name, brand, price, quantity):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Brand: {self.brand}, Price: {self.price}, Quantity: {self.quantity}"
