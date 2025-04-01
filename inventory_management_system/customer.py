# customer.py
from database import connect_db
import os
from utils.helpers import print_store_header

class CustomerInterface:
    def __init__(self):
        self.current_customer_id = None

    def run(self):
        store_name = "Your Store Name"
        print_store_header(store_name)

        while True:
            print("\nCustomer Menu")
            print("1. Register")
            print("2. Search Product")
            print("3. Make Purchase")
            print("4. Exit")
            choice = input("Select an action: ")

            if choice == '1':
                self.register_customer()
            elif choice == '2':
                self.search_product()
            elif choice == '3':
                self.make_purchase()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def register_customer(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
                conn.commit()
                self.current_customer_id = cursor.lastrowid  # Get the ID of the newly registered customer
                print("Registration successful!")
            except sqlite3.IntegrityError:
                print("Email already registered. Please use a different email.")
            conn.close()
        else:
            print("Failed to register due to database connection error.")

    def search_product(self):
        # (Existing search_product code remains unchanged)

    def make_purchase(self):
        if self.current_customer_id is None:
            print("You need to register first.")
            return

        product_id = input("Enter the product ID to purchase: ")
        quantity = input("Enter the quantity to purchase: ")

        try:
            quantity = int(quantity)
        except ValueError:
            print("Invalid quantity. Please enter a numeric value.")
            return

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
            product = cursor.fetchone()

            if product and product[4] >= quantity:  # Check if enough quantity is available
                new_quantity = product[4] - quantity
                cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))

                total_price = product[3] * quantity  # Price * Quantity
                cursor.execute("INSERT INTO purchases (customer_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)",
                               (self.current_customer_id, product_id, quantity, total_price))
                conn.commit()

                # Generate the bill
                self.generate_bill(product, quantity, total_price)

                print("Purchase successful!")
            else:
                print("Insufficient quantity or product not found.")
            conn.close()
        else:
            print("Failed to make purchase due to database connection error.")

    def generate_bill(self, product, quantity, total_price):
        bill_content = (
            f"--- Bill ---\n"
            f"Product ID: {product[0]}\n"
            f"Product Name: {product[1]}\n"
            f"Brand: {product[2]}\n"
            f"Quantity: {quantity}\n"
            f"Total Price: ${total_price:.2f}\n"
            f"Thank you for your purchase!\n"
        )

        # Print the bill to the console
        print(bill_content)

        # Save the bill to a file
        bill_filename = f"bill_{product[0]}_customer_{self.current_customer_id}.txt"
        with open(bill_filename, 'w') as bill_file:
            bill_file.write(bill_content)

        print(f"One copy of the bill has been saved as '{bill_filename}'.")
