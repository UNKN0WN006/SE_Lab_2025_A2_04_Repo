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
    print("___________________________________________________________")
    print(f"| {store_name:^55} |")  
    print("___________________________________________________________")
