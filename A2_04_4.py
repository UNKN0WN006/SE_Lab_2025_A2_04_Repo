import sqlite3
import logging

# Configuring logging
logging.basicConfig(level=logging.INFO)

# Define GST rates based on item types
GST_RATES = {
    'household': 0.18,
    'stationery': 0.12,
    'groceries': 0.05,
    'medicines': 0.18,
}

def connect_db():
    try:
        conn = sqlite3.connect('A2_04_4.db')
        return conn
    except sqlite3.Error as e:
        logging.error(f"Database connection error: {e}")
        return None

def create_tables():
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS item_types (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                gst_rate REAL NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                brand TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                discount REAL DEFAULT 0,
                item_type_id INTEGER,
                FOREIGN KEY (item_type_id) REFERENCES item_types (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                total_price REAL,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')
        conn.commit()
        conn.close()
    else:
        logging.error("Failed to create tables due to database connection error.")

def validate_positive_integer(value):
    """Validate if the input value is a positive integer."""
    try:
        value = int(value)
        if value < 0:
            raise ValueError("Value must be a positive integer.")
        return value
    except ValueError:
        return None

def print_store_header(store_name):
    """Prints a formatted header for the store."""
    print("+" + "-" * 55 + "+")
    print(f"| {store_name:^55} |")  
    print("+" + "-" * 55 + "+")

def print_table_header(headers):
    """Prints a formatted table header."""
    print("+", "-" * 15, "+", "-" * 25, "+", "-" * 10, "+", "-" * 10, "+", "-" * 10, "+")
    print(f"| {'Product ID':<13} | {'Product Name':<23} | {'Price':<8} | {'Quantity':<8} | {'Discount':<8} |")
    print("+", "-" * 15, "+", "-" * 25, "+", "-" * 10, "+", "-" * 10, "+", "-" * 10, "+")

class Customer:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Phone: {self.phone}"

class Product:
    def __init__(self, id, name, brand, price, quantity, discount, item_type_id):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.item_type_id = item_type_id

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Brand: {self.brand}, Price: {self.price}, Quantity: {self.quantity}, Discount: {self.discount}"

class Purchase:
    def __init__(self, product_id, customer_id, quantity):
        self.product_id = product_id
        self.customer_id = customer_id
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Customer ID: {self.customer_id}, Quantity: {self.quantity}"

class CustomerInterface:
    def __init__(self):
        self.current_customer_id = None

    def run(self):
        store_name = "Apex Store"
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
        phone = input("Enter your phone number: ")

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (name, phone))
                conn.commit()
                self.current_customer_id = cursor.lastrowid  # Get the ID of the newly registered customer
                print("Registration successful!")
            except sqlite3.IntegrityError:
                print("Phone number already registered. Please use a different number.")
            conn.close()
        else:
            print("Failed to register due to database connection error.")

    def search_product(self):
        initial = input("Enter the first initial of the product name: ").strip().lower()
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT p.id, p.name, p.brand, p.price, p.quantity, p.discount, it.name FROM products p JOIN item_types it ON p.item_type_id = it.id WHERE LOWER(p.name) LIKE ?", (initial + '%',))
            products = cursor.fetchall()
            conn.close()

            if products:
                print("\nProducts found:")
                print_table_header(["Product ID", "Product Name", "Price", "Quantity", "Discount"])
                for product in products:
                    print(f"| {product[0]:<13} | {product[1]:<23} | {product[3]:<8} | {product[4]:<8} | {product[5]:<8} |")
                print("+", "-" * 15, "+", "-" * 25, "+", "-" * 10, "+", "-" * 10, "+", "-" * 10, "+")
            else:
                print("No products found with that initial.")
        else:
            print("Failed to search products due to database connection error.")

    def make_purchase(self):
        if self.current_customer_id is None:
            print("You need to register first.")
            return

        purchases = {}
        while True:
            product_id = input("Enter the product ID to purchase (or type 'done' to finish): ")
            if product_id.lower() == 'done':
                break

            quantity = input("Enter the quantity to purchase: ")
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                    continue
            except ValueError:
                print("Invalid quantity. Please enter a numeric value.")
                continue

            purchases[product_id] = quantity

        if not purchases:
            print("No items selected for purchase.")
            return

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            total_final_price = 0

            for product_id, quantity in purchases.items():
                cursor.execute("SELECT p.id, p.name, p.price, p.quantity, p.discount, it.name FROM products p JOIN item_types it ON p.item_type_id = it.id WHERE p.id = ?", (product_id,))
                product = cursor.fetchone()

                if product and product[3] >= quantity:  # Check if enough quantity is available
                    new_quantity = product[3] - quantity
                    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))

                    total_price = product[2] * quantity  # Price * Quantity
                    discount_amount = (product[4] / 100) * total_price  # Calculate discount
                    final_price = total_price - discount_amount  # Apply discount
                    gst_rate = GST_RATES.get(product[5], 0)  # Get GST rate based on item type
                    gst_amount = final_price * gst_rate
                    final_price += gst_amount  # Add GST to final price

                    cursor.execute("INSERT INTO purchases (customer_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)",
                                   (self.current_customer_id, product_id, quantity, final_price))
                    total_final_price += final_price

                    # Generate the bill for each product
                    self.generate_bill(product, quantity, discount_amount, total_price, gst_amount, final_price)
                else:
                    print(f"Insufficient quantity for Product ID {product_id} or product not found.")

            print(f"Total amount for all purchases: ${total_final_price:.2f}")
            conn.commit()
            conn.close()
        else:
            print("Failed to make purchase due to database connection error.")

    def generate_bill(self, product, quantity, discount_amount, total_price, gst_amount, final_price):
        bill_content = (
            f"--- Bill ---\n"
            f"+----------------+-----------------------+--------+----------+----------+-------------+\n"
            f"| Product ID     | Product Name          | Price  | Quantity | Discount | Total Price |\n"
            f"+----------------+-----------------------+--------+----------+----------+-------------+\n"
            f"| {product[0]:<14} | {product[1]:<21} | {product[2]:<6} | {quantity:<8} | {discount_amount:<8.2f} | {final_price:<11.2f} |\n"
            f"+----------------+-----------------------+--------+----------+----------+-------------+\n"
            f"| GST ({GST_RATES[product[5]] * 100:.0f}%):    | {gst_amount:<38.2f} |\n"
            f"+----------------+-----------------------+--------+----------+----------+-------------+\n"
            f"Thank you for your purchase!\n"
        )

        # Print the bill to the console
        print(bill_content)

        # Save the bill to a file
        bill_filename = f"bill_{product[0]}_customer_{self.current_customer_id}.txt"
        with open(bill_filename, 'w') as bill_file:
            bill_file.write(bill_content)

        print(f"One copy of the bill has been saved as '{bill_filename}'.")

class ManagerInterface:
    def __init__(self):
        create_tables()
        self.populate_item_types()

    def populate_item_types(self):
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            for item_type, gst_rate in GST_RATES.items():
                cursor.execute("INSERT OR IGNORE INTO item_types (name, gst_rate) VALUES (?, ?)", (item_type, gst_rate))
            conn.commit()
            conn.close()

    def run(self):
        store_name = "Apex Store"
        print_store_header(store_name)

        while True:
            print("\nManager Menu")
            print("1. Add Product")
            print("2. Update Product Discount")
            print("3. View Products")
            print("4. View Customer Purchases")
            print("5. Exit")
            choice = input("Select an action: ")

            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.update_product_discount()
            elif choice == '3':
                self.view_products()
            elif choice == '4':
                self.view_customer_purchases()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def add_product(self):
        name = input("Enter product name: ")
        brand = input("Enter product brand: ")
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")
        item_type_name = input("Enter item type (household, stationery, groceries, medicines): ")

        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")
            return

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM item_types WHERE name = ?", (item_type_name,))
            item_type = cursor.fetchone()

            if item_type:
                cursor.execute("INSERT INTO products (name, brand, price, quantity, item_type_id) VALUES (?, ?, ?, ?, ?)",
                               (name, brand, price, quantity, item_type[0]))
                conn.commit()
                conn.close()
                print("Product added successfully!")
            else:
                print("Invalid item type. Please ensure it is one of the following: household, stationery, groceries, medicines.")
        else:
            print("Failed to add product due to database connection error.")

    def update_product_discount(self):
        product_id = input("Enter the product ID to update the discount: ")
        discount = input("Enter the discount percentage (0-100): ")

        try:
            discount = float(discount)
            if discount < 0 or discount > 100:
                raise ValueError("Discount must be between 0 and 100.")
        except ValueError as e:
            print(f"Invalid discount value: {e}")
            return

        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE products SET discount = ? WHERE id = ?", (discount, product_id))
            conn.commit()
            conn.close()
            print("Discount updated successfully!")
        else:
            print("Failed to update discount due to database connection error.")

    def view_products(self):
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT p.id, p.name, p.brand, p.price, p.quantity, p.discount, it.name FROM products p JOIN item_types it ON p.item_type_id = it.id")
            products = cursor.fetchall()
            conn.close()

            print("\nAvailable Products:")
            print_table_header(["Product ID", "Product Name", "Price", "Quantity", "Discount"])
            for product in products:
                print(f"| {product[0]:<13} | {product[1]:<23} | {product[3]:<8} | {product[4]:<8} | {product[5]:<8.2f} |")
            print("+", "-" * 15, "+", "-" * 25, "+", "-" * 10, "+", "-" * 10, "+", "-" * 10, "+")

        else:
            print("Failed to view products due to database connection error.")

    def view_customer_purchases(self):
        conn = connect_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT c.name, c.phone, p.product_id, p.quantity, p.total_price
                FROM purchases p
                JOIN customers c ON p.customer_id = c.id
            ''')
            purchases = cursor.fetchall()
            conn.close()

            print("\nCustomer Purchases:")
            print("+----------------+----------------+----------+----------+-------------+")
            print("| Customer Name  | Phone          | Product ID | Quantity | Total Price |")
            print("+----------------+----------------+----------+----------+-------------+")
            for purchase in purchases:
                print(f"| {purchase[0]:<15} | {purchase[1]:<14} | {purchase[2]:<10} | {purchase[3]:<8} | ${purchase[4]:<11} |")
            print("+----------------+----------------+----------+----------+-------------+")
        else:
            print("Failed to view customer purchases due to database connection error.")

def main():
    store_name = "Apex Store"
    print_store_header(store_name)

    while True:
        print("\nMain Menu")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")
        choice = input("Select an action: ")

        if choice == '1':
            manager = ManagerInterface()
            manager.run()
        elif choice == '2':
            customer = CustomerInterface()
            customer.run()
        elif choice == '3':
            print("Exiting the application. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
