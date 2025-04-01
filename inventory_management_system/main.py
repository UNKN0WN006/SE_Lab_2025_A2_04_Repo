from manager import ManagerInterface
from customer import CustomerInterface
from utils.helpers import print_store_header

def main():
    store_name = "Your Store Name"
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
