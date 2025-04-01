from database import create_tables, connect_db
import logging
from utils.helpers import print_store_header

class ManagerInterface:
    def __init__(self):
        create_tables()

    def run(self):
        store_name = "Your Store Name"
        print_store_header(store_name)

        while True:
            print("\nManager Menu")
            print("1. Add Product")
            print("2. View Products")
            print("3. View Customer Purchases")
            print("4. Exit")
            choice = input("Select an action: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.view_products()
            elif choice == '3':
                self.view_customer_purchases()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_product(self):
        name = input("Enter product name: ")
        brand = input("Enter product brand: ")
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")

        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")
            return

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, brand, price, quantity) VALUES (?, ?, ?, ?)",
                           (name, brand, price, quantity))
            conn.commit()
            conn.close()
            print("Product added successfully!")
        else:
            print("Failed to add product due to database connection error.")

    def view_products(self):
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
            conn.close()

            print("\nAvailable Products:")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Brand: {product[2]}, Price: {product[3]}, Quantity: {product[4]}")
        else:
            print("Failed to view products due to database connection error.")

    def view_customer_purchases(self):
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT c.name, c.email, p.product_id, p.quantity, p.total_price
                FROM purchases p
                JOIN customers c ON p.customer_id = c.id
            ''')
            purchases = cursor.fetchall()
            conn.close()

            print("\nCustomer Purchases:")
            for purchase in purchases:
                print(f"Customer Name: {purchase[0]}, Email: {purchase[1]}, Product ID: {purchase[2]}, Quantity: {purchase[3]}, Total Price: ${purchase[4]:.2f}")
        else:
            print("Failed to view customer purchases due to database connection error.")
