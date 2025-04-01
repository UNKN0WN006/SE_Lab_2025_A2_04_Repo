# Inventory Management System

## Overview

The Inventory Management System is a console-based application designed to help manage products in a store, track customer registrations, and log purchases. This system allows managers to add products, view inventory, and see customer purchase history, while customers can register, search for products, and make purchases.

## Project Structure
```bash
inventory_management_system/
│
├── README.md
├── requirements.txt
├── main.py
├── database.py
├── manager.py
├── customer.py
├── models/
│  ├── __init__.py
│  ├── product.py
│  ├── customer.py
│  └── purchase.py
└── utils/
    ├── __init__.py
    └── helpers.py

```

## File Descriptions

- **database.py**: This file manages the SQLite database connection and defines the schema for the products, customers, and purchases tables. It includes functions to connect to the database and create necessary tables.

- **main.py**: The main entry point of the application. It provides a menu for users to choose between manager and customer interfaces.

- **manager.py**: Contains the `ManagerInterface` class, which allows managers to add products, view the inventory, and see customer purchases.

- **customer.py**: Contains the `CustomerInterface` class, which allows customers to register, search for products, and make purchases.

- **utils/__init__.py**: This file is intentionally left empty. It indicates that the `utils` directory is a package. This is a common practice in Python to allow for better organization of code.

- **utils/helpers.py**: Contains utility functions that can be reused throughout the application, such as printing a formatted store header.

- **requirements.txt**: This file lists the dependencies required for the project. Currently, there are no external dependencies, so it is empty. If you decide to use any external libraries in the future (e.g., for logging, testing, or database management), you can add them here.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hembramsushar/SE-lab-2025-A2-04-Repo.git
   cd inventory_management_system
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies (if any are added in the future):
   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run the application, execute the following command:
```bash
python main.py
```

Follow the on-screen instructions to navigate through the manager and customer interfaces.


### Explanation of the README Sections

- **Overview**: Provides a brief description of what the project does.
- **Project Structure**: Lists the files and directories in the project, along with a brief description of each.
- **File Descriptions**: Gives detailed information about the purpose of each file.
- **Installation**: Instructions on how to set up the project locally.
- **Usage**: How to run the application.
- **Contributing**: Guidelines for contributing to the project.
- **License**: Information about the project's licensing.

### Conclusion

If you have any further questions or need additional assistance, let me know!

## Troubleshooting

If you encounter any issues while running the application, consider the following steps:

1. **Database Connection Issues**: Ensure that the SQLite database is accessible and that the necessary tables have been created. If you encounter errors related to database connections, check the `database.py` file for any issues in the connection logic.

2. **Indentation Errors**: Python is sensitive to indentation. If you see `IndentationError`, check your code for inconsistent use of spaces and tabs.

3. **Missing Dependencies**: If you add any external libraries in the future, ensure they are listed in `requirements.txt` and installed in your environment.

4. **General Errors**: Review the error messages in the console for clues. If you need further assistance, consider reaching out to the project maintainers or checking online forums.

## Future Enhancements

Here are some potential enhancements that could be made to the Inventory Management System:

1. **User  Authentication**: Implement user authentication for both managers and customers to enhance security.

2. **Graphical User Interface (GUI)**: Develop a GUI using libraries like Tkinter or PyQt to make the application more user-friendly.

3. **Reporting Features**: Add reporting capabilities to generate sales reports, inventory reports, and customer activity logs.

4. **Unit Testing**: Implement unit tests to ensure the reliability of the code and facilitate future development.

5. **Deployment**: Consider deploying the application as a web service using frameworks like Flask or Django for broader accessibility.

## Acknowledgments

- **SQLite**: For providing a lightweight database solution that is easy to integrate and use.
- **Python**: For being a versatile programming language that allows for rapid development and prototyping.
- **Open Source Community**: For the countless resources and libraries that make development easier and more efficient.

## Contact

For any questions or feedback, please contact:

- **Name**: [hembramsushar@gmail.com](mailto:hembramsushar@gmail.com)
- **GitHub Profile**: [Sushar Hembram](https://github.com/hembramsushar)

Thank you for using the Inventory Management System!
